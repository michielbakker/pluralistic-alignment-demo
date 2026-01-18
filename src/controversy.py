"""
Controversy detection module.

Determines whether a query is controversial along different dimensions
(religious, political, regional) and whether perspectives should be surfaced.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional
import re


class ControversyLevel(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class ControversyProfile:
    """Profile indicating controversy levels across different dimensions."""
    religious: ControversyLevel
    political: ControversyLevel
    regional: ControversyLevel

    def should_surface_perspectives(self) -> bool:
        """Determine if perspectives should be surfaced based on controversy levels."""
        # Surface if any dimension is medium or high
        high_controversy = {ControversyLevel.MEDIUM, ControversyLevel.HIGH}
        return (
            self.religious in high_controversy or
            self.political in high_controversy or
            self.regional in high_controversy
        )

    def max_controversy_level(self) -> ControversyLevel:
        """Return the highest controversy level across dimensions."""
        levels = [self.religious, self.political, self.regional]
        if ControversyLevel.HIGH in levels:
            return ControversyLevel.HIGH
        if ControversyLevel.MEDIUM in levels:
            return ControversyLevel.MEDIUM
        if ControversyLevel.LOW in levels:
            return ControversyLevel.LOW
        return ControversyLevel.NONE


# Topic patterns mapped to controversy profiles
# This is a rule-based classifier using keyword matching
TOPIC_PATTERNS = {
    # Reproductive rights - high religious & political
    "reproductive_rights": {
        "patterns": [
            r"\babortion\b", r"\breproductive\s+rights?\b", r"\bpro[- ]?(life|choice)\b",
            r"\broe\s+v\.?\s*wade\b", r"\bpregnancy\s+termination\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.HIGH,
            regional=ControversyLevel.LOW
        )
    },

    # Climate/environment - political & regional
    "climate_environment": {
        "patterns": [
            r"\bclimate\s+change\b", r"\bglobal\s+warming\b", r"\bclimate\s+policy\b",
            r"\benvironmental\s+(policy|protection)\b", r"\bcarbon\s+(tax|emissions?)\b",
            r"\bgreen\s+new\s+deal\b", r"\bclimate\s+science\b", r"\bclimate\b",
            r"\benvironment\s+and\s+development\b", r"\baddress\s+climate\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.LOW,
            political=ControversyLevel.HIGH,
            regional=ControversyLevel.MEDIUM
        )
    },

    # Church-state separation - high religious & medium political
    "church_state_separation": {
        "patterns": [
            r"\breligious\s+symbols?\b", r"\bpublic\s+school.{0,20}(prayer|religious)\b",
            r"\bchurch\s+and\s+state\b", r"\bsecularism\b", r"\blaicit[eé]\b",
            r"\breligious\s+(clothing|dress|headwear)\b", r"\bhijab\b", r"\bturban\b",
            r"\bburqa\b", r"\breligious\s+freedom\b", r"\bprayer.{0,20}(school|public)\b",
            r"\bschool.{0,20}prayer\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.MEDIUM,
            regional=ControversyLevel.HIGH
        )
    },

    # Animal rights / food ethics - religious dimension
    "animal_rights_religious_law": {
        "patterns": [
            r"\bcows?\s+(be\s+)?protected\b", r"\bcow\s+protection\b",
            r"\bethics\s+of\s+cow\b", r"\bprotect.{0,10}cows?\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.LOW,
            regional=ControversyLevel.HIGH
        )
    },

    "food_ethics_animal_rights": {
        "patterns": [
            r"\b(eat|eating)\s+(meat|animals?)\b", r"\bvegetarian(ism)?\b", r"\bvegan(ism)?\b",
            r"\banimal\s+rights?\b", r"\bhalal\b", r"\bkosher\b",
            r"\bdietary\s+law\b", r"\bethics\s+of\s+(eating|food)\b", r"\bethical\s+to\s+eat\b",
            r"\bstop\s+eating\s+animals\b", r"\barguments?\s+for\s+vegetarian\b",
            r"\breligions?\s+view.{0,20}(meat|eating)\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.LOW,
            regional=ControversyLevel.MEDIUM
        )
    },

    # Economic policy (UBI) - political
    "economic_policy": {
        "patterns": [
            r"\buniversal\s+basic\s+income\b", r"\bUBI\b", r"\bwelfare\s+(state|system)\b",
            r"\bredistribution\b", r"\bminimum\s+wage\b", r"\bsocialism\b",
            r"\bcapitalism\b", r"\bfree\s+market\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.LOW,
            political=ControversyLevel.HIGH,
            regional=ControversyLevel.LOW
        )
    },

    # LGBTQ rights - high religious & political
    "LGBTQ_rights": {
        "patterns": [
            r"\bsame[- ]sex\s+marriage\b", r"\bgay\s+marriage\b", r"\bLGBTQ?\+?\b",
            r"\bhomosexual(ity)?\b", r"\btransgender\b", r"\bgender\s+identity\b",
            r"\bsexual\s+orientation\b", r"\bmarriage\s+equality\b",
            r"\bgovernment.{0,20}marriage\b", r"\bmarriage.{0,20}(legal|government)\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.HIGH,
            regional=ControversyLevel.LOW
        )
    },

    # Gun rights - political
    "gun_rights": {
        "patterns": [
            r"\bgun\s+control\b", r"\bgun\s+rights?\b", r"\b2nd\s+amendment\b",
            r"\bsecond\s+amendment\b", r"\bfirearm\s+regulation\b", r"\bgun\s+violence\b",
            r"\bgun\s+laws?\b", r"\bweapon\s+ban\b", r"\bgun\s+polic(y|ies)\b",
            r"\bprevent\s+gun\s+violence\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.LOW,
            political=ControversyLevel.HIGH,
            regional=ControversyLevel.MEDIUM
        )
    },

    # Indigenous rights - regional
    "indigenous_rights_environment": {
        "patterns": [
            r"\bindigenous\s+(rights?|lands?|peoples?)\b", r"\bnative\s+(american|rights?|lands?)\b",
            r"\btribal\s+(sovereignty|lands?)\b", r"\bland\s+rights?\b",
            r"\bproperty\s+rights?.{0,20}environment\b", r"\bprotect.{0,20}(land|development)\b",
            r"\benvironment.{0,20}development\b", r"\bdevelopment.{0,20}environment\b",
            r"\bbalance.{0,20}(environment|development)\b", r"\bjobs?.{0,20}land\b",
            r"\bland.{0,20}jobs?\b", r"\becological.{0,20}importance\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.MEDIUM,
            political=ControversyLevel.MEDIUM,
            regional=ControversyLevel.HIGH
        )
    },

    # Immigration - political & regional
    "immigration": {
        "patterns": [
            r"\bimmigra(tion|nt)\b", r"\bundocumented\b", r"\billegal\s+alien\b",
            r"\bborder\s+(security|wall|control)\b", r"\bdeport(ation)?\b",
            r"\bcitizenship\s+path\b", r"\brefugee\b", r"\basylum\b", r"\bvisa\b",
            r"\bsecure\s+the\s+border\b", r"\bborder\s+communit(y|ies)\b",
            r"\bamerican\s+identity\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.LOW,
            political=ControversyLevel.HIGH,
            regional=ControversyLevel.HIGH
        )
    },

    # Disability rights - should surface perspectives (medium controversy for community)
    "disability_rights": {
        "patterns": [
            r"\bautism\b", r"\bdisability\s+rights?\b", r"\bneurodiver(gent|sity)\b",
            r"\bperson[- ]first\s+language\b", r"\bidentity[- ]first\b",
            r"\bspecial\s+needs?\b", r"\baccommodations?\b", r"\bautistic\b",
            r"\bcured?\b.{0,20}autism\b", r"\bautism.{0,20}cured?\b",
            r"\bhelp.{0,20}autistic\b", r"\bcauses?\s+autism\b",
            r"\bsupport.{0,20}neurodivergent\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.LOW,
            political=ControversyLevel.LOW,
            regional=ControversyLevel.MEDIUM  # Changed to MEDIUM to trigger perspective surfacing
        )
    },

    # Gender & religious freedom (hijab, etc)
    "gender_religious_freedom": {
        "patterns": [
            r"\bhijab\b", r"\bburqa\b", r"\bniqab\b", r"\bheadscarf\b",
            r"\bwomen.{0,20}(wear|required|forced)\b", r"\breligious\s+dress\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.MEDIUM,
            regional=ControversyLevel.HIGH
        )
    },

    # Religious law
    "religious_law": {
        "patterns": [
            r"\breligious\s+law\b", r"\bsharia\b", r"\bchurch\s+law\b",
            r"\breligious.{0,20}(state|enforced)\b", r"\btheocra(cy|tic)\b",
            r"\bdietary\s+laws?.{0,20}(state|enforced)\b"
        ],
        "profile": ControversyProfile(
            religious=ControversyLevel.HIGH,
            political=ControversyLevel.MEDIUM,
            regional=ControversyLevel.LOW
        )
    },
}

# Factual/non-controversial patterns
FACTUAL_PATTERNS = [
    r"\bcapital\s+of\b",
    r"\bhow\s+(do|to)\s+(make|cook|write|code|program)\b",
    r"\bwhat\s+time\b",
    r"\bwho\s+won\b",
    r"\bfor\s+loop\b",
    r"\brecipe\b",
    r"\bprogramming\b",
    r"\bsyntax\b",
]


def detect_controversy(query: str) -> tuple[ControversyProfile, Optional[str]]:
    """
    Detect controversy level of a query.

    Returns:
        Tuple of (ControversyProfile, topic_category or None)
    """
    query_lower = query.lower()

    # First check if it's a simple factual question
    for pattern in FACTUAL_PATTERNS:
        if re.search(pattern, query_lower, re.IGNORECASE):
            return ControversyProfile(
                religious=ControversyLevel.NONE,
                political=ControversyLevel.NONE,
                regional=ControversyLevel.NONE
            ), None

    # Check against topic patterns
    for topic_category, topic_data in TOPIC_PATTERNS.items():
        for pattern in topic_data["patterns"]:
            if re.search(pattern, query_lower, re.IGNORECASE):
                return topic_data["profile"], topic_category

    # Default: low controversy, no specific category
    return ControversyProfile(
        religious=ControversyLevel.LOW,
        political=ControversyLevel.LOW,
        regional=ControversyLevel.LOW
    ), None


def get_controversy_dimensions(profile: ControversyProfile) -> list[str]:
    """Get list of dimensions where controversy is medium or high."""
    dimensions = []
    if profile.religious in {ControversyLevel.MEDIUM, ControversyLevel.HIGH}:
        dimensions.append("religious")
    if profile.political in {ControversyLevel.MEDIUM, ControversyLevel.HIGH}:
        dimensions.append("political")
    if profile.regional in {ControversyLevel.MEDIUM, ControversyLevel.HIGH}:
        dimensions.append("regional")
    return dimensions
