# Synthetic Dataset Data Dictionary

## Overview
This synthetic dataset contains 60 test cases for evaluating a perspective surfacing system. It includes user profiles with community affiliations and queries designed to test various aspects of the system.

## File Structure
- **Format:** CSV (Comma-Separated Values)
- **Records:** 60 user-query pairs
- **Purpose:** Testing consistency, coverage, appropriateness, and representation accuracy

---

## Field Definitions

### User Profile Fields

#### `user_id`
- **Type:** String
- **Format:** U### (e.g., U001, U002)
- **Description:** Unique identifier for each user-query pair
- **Usage:** Track consistency across similar users/queries

#### `primary_community_type`
- **Type:** String
- **Values:** religious, secular, political, identity, regional, professional
- **Description:** The category of the user's strongest community affiliation
- **Usage:** Determines which tier to prioritize in perspective selection

#### `primary_community`
- **Type:** String
- **Examples:** Hindu, Catholic, progressive, LGBTQ_gay, working_class
- **Description:** The specific community the user most strongly identifies with
- **Usage:** User's baseline perspective; system should represent this accurately

#### `community_strength`
- **Type:** String
- **Values:** core, moderate, peripheral
- **Description:** How strongly the user identifies with their primary community
- **Usage:** 
  - core = central to identity, highly engaged
  - moderate = important but not defining
  - peripheral = aware/interested but not deeply engaged

#### `secondary_community_type`
- **Type:** String
- **Values:** Same as primary_community_type
- **Description:** Category of second most important affiliation
- **Nullable:** Can be empty if user has only one strong affiliation

#### `secondary_community`
- **Type:** String
- **Description:** Specific secondary community
- **Usage:** Adds nuance; user may have multiple relevant perspectives

#### `secondary_strength`
- **Type:** String
- **Values:** core, moderate, peripheral
- **Description:** Strength of secondary affiliation

#### `tertiary_community_type`
- **Type:** String
- **Description:** Category of third affiliation (if any)

#### `tertiary_community`
- **Type:** String
- **Description:** Specific tertiary community

#### `age_range`
- **Type:** String
- **Format:** ##-## (e.g., 25-35, 35-45)
- **Description:** User's age bracket
- **Usage:** May be relevant for certain topics (e.g., generational perspectives)

#### `education`
- **Type:** String
- **Values:** high_school, some_college, bachelors, graduate, masters, phd
- **Description:** Highest education level completed
- **Usage:** Can indicate epistemic preferences (e.g., academic vs experiential knowledge)

#### `location`
- **Type:** String
- **Format:** descriptor_region (e.g., urban_US, rural_India)
- **Description:** Geographic context
- **Usage:** Regional perspectives, urban/rural divides

---

### Query Fields

#### `query_id`
- **Type:** String
- **Format:** Q### (e.g., Q001, Q002)
- **Description:** Unique identifier for each query
- **Usage:** Track queries, link to expected behaviors

#### `query_text`
- **Type:** String
- **Description:** The actual question/query the user asks
- **Usage:** Input to the perspective surfacing system

#### `topic_category`
- **Type:** String
- **Examples:** animal_rights_religious_law, reproductive_rights, climate_environment
- **Description:** Semantic category of the query
- **Usage:** Group similar queries for analysis

---

### Controversy Profile Fields

#### `controversy_religious`
- **Type:** String
- **Values:** none, low, medium, high
- **Description:** Degree of controversy along religious cleavages
- **Interpretation:**
  - none = No religious disagreement
  - low = Minor differences between traditions
  - medium = Significant but not central disagreement
  - high = Core religious issue with strong opposing views

#### `controversy_political`
- **Type:** String
- **Values:** none, low, medium, high
- **Description:** Degree of controversy along political/ideological cleavages
- **Interpretation:** Same scale as religious

#### `controversy_regional`
- **Type:** String
- **Values:** none, low, medium, high
- **Description:** Degree of controversy along geographic/cultural cleavages
- **Examples:** 
  - high = US vs Middle East, Global North vs South
  - low = Relatively universal agreement across regions

---

### Expected Behavior Fields

#### `should_surface_perspectives`
- **Type:** String
- **Values:** yes, no
- **Description:** Whether the system should surface multiple perspectives
- **Logic:** 
  - "yes" if any controversy dimension is medium-high AND strongly held views differ
  - "no" for simple factual questions or non-controversial topics

#### `selected_communities`
- **Type:** String
- **Format:** Comma-separated list (e.g., "Hindu_traditional,secular_liberal,Indian_regional")
- **Description:** Which community perspectives should be surfaced
- **Interpretation:**
  - First item is typically user's own community (baseline)
  - Subsequent items are other relevant perspectives
  - Order may suggest priority/prominence
- **Special Value:** "N/A" when should_surface_perspectives = no

---

### Testing Fields

#### `consistency_group`
- **Type:** String
- **Description:** Identifier for queries that should receive consistent perspective framing
- **Usage:** 
  - Users in same consistency_group should see identical framings of other perspectives
  - Example: U001 and U002 are both Hindu users asking about cow protection → should get same framing of secular perspective
- **Testing:** Calculate semantic similarity of perspective descriptions across same group

#### `notes`
- **Type:** String (free text)
- **Description:** Additional context, testing rationale, or special considerations
- **Examples:**
  - "Hindu user - should get consistent framing of secular view"
  - "LGBTQ person directly affected"
  - "Simple factual - no perspectives needed"
- **Usage:** Explains test case purpose, flags edge cases, provides evaluator guidance

---

## Test Case Categories

### Consistency Tests (Same Community, Same Topic)
- **Examples:** U001-U002 (Hindu, cow protection), U004-U006 (abortion, religious conservative)
- **Purpose:** Verify users from same community get consistent framings
- **Evaluation:** High semantic similarity in perspective descriptions

### Coverage Tests (Multiple Relevant Communities)
- **Examples:** Q007 (multi-faith abortion), Q020 (religions and meat)
- **Purpose:** Verify all major relevant perspectives are included
- **Evaluation:** Recall of ground truth communities

### Appropriateness Tests (Should/Shouldn't Surface)
- **Examples:** Q051-Q055 (factual questions → no surfacing), Q026-Q029 (controversial → yes surfacing)
- **Purpose:** Verify correct triggering of perspective surfacing
- **Evaluation:** Precision/Recall on surfacing decision

### Affected Community Tests (Tier 5 Sensitivity)
- **Examples:** U026 (LGBTQ person on marriage), U037 (gun violence survivor), U041 (indigenous on land rights)
- **Purpose:** Verify directly affected communities are prioritized
- **Evaluation:** Affected community perspective is included and given prominence

### Cross-Cleavage Tests (Controversial in One Dimension)
- **Examples:** Q001 (religious but not political), Q010 (political but not religious)
- **Purpose:** Verify system distinguishes controversy types
- **Evaluation:** Correct identification of which cleavage is active

### Reframing Tests (Different Angle on Same Issue)
- **Examples:** U008 (libertarian on abortion = government power), U029 (libertarian on marriage = government role)
- **Purpose:** Verify system adapts to user's framework
- **Evaluation:** Perspective framing matches user's primary concern

### Edge Cases
- **Examples:** U028 (progressive Catholic - internal tension), U033 (Muslim feminist - intersectional)
- **Purpose:** Test handling of users with potentially conflicting affiliations
- **Evaluation:** Respectful representation of both identities

---

## Usage Guidelines

### For Consistency Evaluation
1. Group records by `consistency_group`
2. For each group, extract system-generated perspective descriptions
3. Calculate semantic similarity (e.g., cosine similarity of embeddings)
4. Target: >0.85 similarity within groups

### For Coverage Evaluation
1. For each record where `should_surface_perspectives = yes`
2. Parse `selected_communities` into ground truth list
3. Extract communities mentioned in system output
4. Calculate recall: |intersection| / |ground truth|
5. Target: >0.90 recall

### For Appropriateness Evaluation
1. Create binary classifier: should_surface_perspectives (yes/no)
2. Compare system decision to ground truth
3. Calculate precision and recall
4. Target: Precision >0.85, Recall >0.80

### For Representation Accuracy
1. Sample records from each major community
2. Show system outputs to community members
3. Collect ratings: "Does this accurately represent your community's view?" (1-5 scale)
4. Target: Mean rating >4.0

---

## Stratification Summary

### By Community Type
- **Religious:** 20 users (Catholic, Hindu, Muslim, Buddhist, Jewish, Evangelical, Sikh)
- **Secular:** 12 users (Atheist, Agnostic)
- **Political:** 15 users (Progressive, Conservative, Libertarian, Socialist)
- **Identity:** 13 users (LGBTQ, Working class, Parent, Immigrant, Disability, etc.)

### By Topic
- **Reproductive Rights:** 8 queries
- **Climate/Environment:** 5 queries
- **Church-State Separation:** 5 queries
- **Animal Rights/Food Ethics:** 5 queries
- **Economic Policy (UBI):** 5 queries
- **LGBTQ Rights:** 5 queries
- **Gun Rights:** 5 queries
- **Indigenous Rights:** 5 queries
- **Immigration:** 5 queries
- **Disability Rights:** 5 queries
- **Simple Factual (Control):** 5 queries
- **Other:** 7 queries

### By Controversy Level
- **High Controversy (any dimension):** 35 queries
- **Medium Controversy:** 12 queries
- **Low/No Controversy:** 13 queries

### By Should Surface Perspectives
- **Yes (should surface):** 55 queries
- **No (simple factual):** 5 queries

---

## Known Limitations

1. **US-Centric Bias:** Most users located in US; limited international representation
2. **English-Only:** All queries in English
3. **Binary Choices:** Many issues presented with 2-3 main perspectives (real world more complex)
4. **Static Communities:** No users with recently changed affiliations
5. **Limited Intersectionality:** Most users have 2-3 communities; real users more complex
6. **Synthetic Nature:** Queries may not reflect natural language patterns

---

## Future Enhancements

1. Add non-US users for more geographic diversity
2. Include queries in multiple languages
3. Add temporal dimension (how perspectives change over time)
4. Include more intersectional test cases
5. Add adversarial examples (trying to game the system)
6. Include ambiguous queries where controversy is unclear
