"""
Community definitions and tier system for perspective surfacing.

Tier 1: Major world religions & secular worldviews (hard-coded, always available)
Tier 2: Political & ideological orientations (hard-coded, context-dependent)
Tier 3: Regional & cultural communities (model-selected)
Tier 4: Professional & epistemic communities (model-selected)
Tier 5: Identity & experience-based communities (high sensitivity)
Tier 6: Issue-specific & activist communities (query-dependent)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class CommunityTier(Enum):
    TIER_1_RELIGIOUS = 1
    TIER_2_POLITICAL = 2
    TIER_3_REGIONAL = 3
    TIER_4_PROFESSIONAL = 4
    TIER_5_IDENTITY = 5
    TIER_6_ISSUE_SPECIFIC = 6


class Sensitivity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Community:
    id: str
    name: str
    tier: CommunityTier
    sensitivity: Sensitivity
    parent: Optional[str] = None  # For sub-communities
    description: Optional[str] = None


# Tier 1: Major World Religions & Secular Worldviews
TIER_1_COMMUNITIES = {
    # Christianity
    "Catholic": Community("Catholic", "Catholic", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Christian"),
    "evangelical_protestant": Community("evangelical_protestant", "Evangelical Protestant", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Christian"),
    "mainline_protestant": Community("mainline_protestant", "Mainline Protestant", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Christian"),
    "Orthodox_Christian": Community("Orthodox_Christian", "Orthodox Christian", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Christian"),

    # Islam
    "Muslim_Sunni": Community("Muslim_Sunni", "Sunni Muslim", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Muslim"),
    "Muslim_Shia": Community("Muslim_Shia", "Shia Muslim", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Muslim"),

    # Hinduism
    "Hindu": Community("Hindu", "Hindu", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM),
    "Hindu_traditional": Community("Hindu_traditional", "Traditional Hindu", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Hindu"),

    # Buddhism
    "Buddhist": Community("Buddhist", "Buddhist", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM),
    "Buddhist_Theravada": Community("Buddhist_Theravada", "Theravada Buddhist", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Buddhist"),
    "Buddhist_Mahayana": Community("Buddhist_Mahayana", "Mahayana Buddhist", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Buddhist"),

    # Judaism
    "Jewish_Orthodox": Community("Jewish_Orthodox", "Orthodox Jewish", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Jewish"),
    "Jewish_Conservative": Community("Jewish_Conservative", "Conservative Jewish", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Jewish"),
    "reform_jewish": Community("reform_jewish", "Reform Jewish", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM, "Jewish"),

    # Sikhism
    "Sikh": Community("Sikh", "Sikh", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM),

    # Jainism
    "Jain": Community("Jain", "Jain", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.MEDIUM),

    # Secular/Non-religious
    "atheist": Community("atheist", "Atheist", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.LOW),
    "agnostic": Community("agnostic", "Agnostic", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.LOW),
    "spiritual_not_religious": Community("spiritual_not_religious", "Spiritual but not Religious", CommunityTier.TIER_1_RELIGIOUS, Sensitivity.LOW),
}

# Tier 2: Political & Ideological Orientations
TIER_2_COMMUNITIES = {
    # Primary political axes
    "progressive": Community("progressive", "Progressive", CommunityTier.TIER_2_POLITICAL, Sensitivity.MEDIUM),
    "conservative": Community("conservative", "Conservative", CommunityTier.TIER_2_POLITICAL, Sensitivity.MEDIUM),
    "libertarian": Community("libertarian", "Libertarian", CommunityTier.TIER_2_POLITICAL, Sensitivity.MEDIUM),
    "moderate": Community("moderate", "Moderate/Centrist", CommunityTier.TIER_2_POLITICAL, Sensitivity.LOW),
    "socialist": Community("socialist", "Socialist", CommunityTier.TIER_2_POLITICAL, Sensitivity.MEDIUM),

    # Specific ideological frameworks
    "environmentalist": Community("environmentalist", "Environmentalist", CommunityTier.TIER_2_POLITICAL, Sensitivity.LOW),
    "feminist": Community("feminist", "Feminist", CommunityTier.TIER_2_POLITICAL, Sensitivity.MEDIUM),
}

# Tier 3: Regional & Cultural Communities
TIER_3_COMMUNITIES = {
    # Geographic regions
    "urban_US": Community("urban_US", "Urban US", CommunityTier.TIER_3_REGIONAL, Sensitivity.LOW),
    "rural_US": Community("rural_US", "Rural US", CommunityTier.TIER_3_REGIONAL, Sensitivity.LOW),
    "suburban_US": Community("suburban_US", "Suburban US", CommunityTier.TIER_3_REGIONAL, Sensitivity.LOW),
    "Global_South": Community("Global_South", "Global South", CommunityTier.TIER_3_REGIONAL, Sensitivity.MEDIUM),
    "Global_North": Community("Global_North", "Global North", CommunityTier.TIER_3_REGIONAL, Sensitivity.LOW),

    # Diaspora communities
    "South_Asian_diaspora": Community("South_Asian_diaspora", "South Asian Diaspora", CommunityTier.TIER_3_REGIONAL, Sensitivity.MEDIUM),
    "Middle_East_diaspora": Community("Middle_East_diaspora", "Middle Eastern Diaspora", CommunityTier.TIER_3_REGIONAL, Sensitivity.MEDIUM),
    "Latin_American_diaspora": Community("Latin_American_diaspora", "Latin American Diaspora", CommunityTier.TIER_3_REGIONAL, Sensitivity.MEDIUM),
    "Asian_American": Community("Asian_American", "Asian American", CommunityTier.TIER_3_REGIONAL, Sensitivity.MEDIUM),

    # Specific regions
    "border_state": Community("border_state", "US Border State", CommunityTier.TIER_3_REGIONAL, Sensitivity.LOW),
    "border_community": Community("border_community", "Border Community", CommunityTier.TIER_3_REGIONAL, Sensitivity.MEDIUM),
}

# Tier 4: Professional & Epistemic Communities
TIER_4_COMMUNITIES = {
    "scientist": Community("scientist", "Scientist", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "climate_scientist": Community("climate_scientist", "Climate Scientist", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "economist": Community("economist", "Economist", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "educator": Community("educator", "Educator", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "law_enforcement": Community("law_enforcement", "Law Enforcement", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.MEDIUM),
    "medical_researcher": Community("medical_researcher", "Medical Researcher", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "tech_entrepreneur": Community("tech_entrepreneur", "Tech Entrepreneur", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "software_engineer": Community("software_engineer", "Software Engineer", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
    "environmental_scientist": Community("environmental_scientist", "Environmental Scientist", CommunityTier.TIER_4_PROFESSIONAL, Sensitivity.LOW),
}

# Tier 5: Identity & Experience-Based Communities
TIER_5_COMMUNITIES = {
    # Age-based
    "youth": Community("youth", "Youth (under 25)", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),
    "parent": Community("parent", "Parent", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),
    "parent_of_disabled": Community("parent_of_disabled", "Parent of Disabled Child", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),

    # Gender & Sexuality
    "women": Community("women", "Women", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),
    "LGBTQ_gay": Community("LGBTQ_gay", "LGBTQ+ (Gay)", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),
    "LGBTQ_transgender": Community("LGBTQ_transgender", "LGBTQ+ (Transgender)", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),

    # Disability & Health
    "neurodivergent": Community("neurodivergent", "Neurodivergent", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),
    "disability_rights_advocate": Community("disability_rights_advocate", "Disability Rights Advocate", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),

    # Socioeconomic
    "working_class": Community("working_class", "Working Class", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),
    "labor_union": Community("labor_union", "Labor/Union", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),
    "business_owner": Community("business_owner", "Business Owner", CommunityTier.TIER_5_IDENTITY, Sensitivity.LOW),

    # Immigration
    "immigrant": Community("immigrant", "Immigrant", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),
    "second_generation": Community("second_generation", "Second Generation Immigrant", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),

    # Racial/Ethnic
    "indigenous": Community("indigenous", "Indigenous", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),

    # Experience-based
    "gun_owner": Community("gun_owner", "Gun Owner", CommunityTier.TIER_5_IDENTITY, Sensitivity.MEDIUM),
    "gun_violence_survivor": Community("gun_violence_survivor", "Gun Violence Survivor", CommunityTier.TIER_5_IDENTITY, Sensitivity.HIGH),
    "vegetarian": Community("vegetarian", "Vegetarian", CommunityTier.TIER_5_IDENTITY, Sensitivity.LOW),
    "omnivore": Community("omnivore", "Omnivore", CommunityTier.TIER_5_IDENTITY, Sensitivity.LOW),
    "local_community": Community("local_community", "Local Community Member", CommunityTier.TIER_5_IDENTITY, Sensitivity.LOW),
}

# Tier 6: Issue-Specific & Activist Communities
TIER_6_COMMUNITIES = {
    "animal_rights_activist": Community("animal_rights_activist", "Animal Rights Activist", CommunityTier.TIER_6_ISSUE_SPECIFIC, Sensitivity.MEDIUM),
}

# Combined dictionary of all communities
ALL_COMMUNITIES = {
    **TIER_1_COMMUNITIES,
    **TIER_2_COMMUNITIES,
    **TIER_3_COMMUNITIES,
    **TIER_4_COMMUNITIES,
    **TIER_5_COMMUNITIES,
    **TIER_6_COMMUNITIES,
}


def get_community(community_id: str) -> Optional[Community]:
    """Get a community by its ID."""
    return ALL_COMMUNITIES.get(community_id)


def get_community_name(community_id: str) -> str:
    """Get the display name for a community."""
    community = get_community(community_id)
    if community:
        return community.name
    # Fallback: convert ID to title case
    return community_id.replace("_", " ").title()


def get_communities_by_tier(tier: CommunityTier) -> dict[str, Community]:
    """Get all communities in a specific tier."""
    return {k: v for k, v in ALL_COMMUNITIES.items() if v.tier == tier}
