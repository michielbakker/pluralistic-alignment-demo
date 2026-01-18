# Community Tier List for Perspective Surfacing

## Tier 1: Major World Religions & Secular Worldviews
*Hard-coded, always available, highest priority*

### Religious Traditions

**Christianity**
- Catholic
- Protestant (Evangelical, Mainline)
- Orthodox (Eastern, Oriental)

**Islam**
- Sunni
- Shia

**Hinduism**
- Vaishnavite
- Shaivite
- Secular/Cultural Hindu

**Buddhism**
- Theravada
- Mahayana
- Vajrayana

**Judaism**
- Orthodox
- Conservative
- Reform

**Sikhism**

### Secular/Non-religious
- Secular/Atheist
- Agnostic
- Spiritual but not religious

**Rationale:** These represent major global worldviews with distinct ethical frameworks. Missing any of these would be a significant representation gap.

---

## Tier 2: Political & Ideological Orientations
*Hard-coded, context-dependent activation*

### Primary Political Axes

**Progressive/Left**
- Democratic Socialist
- Social Liberal

**Conservative/Right**
- Social Conservative
- Fiscal Conservative

**Libertarian**
- Left-libertarian
- Right-libertarian

**Centrist/Moderate**

### Specific Ideological Frameworks
- Environmentalist/Green
- Nationalist/Populist
- Feminist (various waves/branches)
- Socialist/Communist
- Classical Liberal

**Rationale:** Political orientation strongly predicts views on contested issues. These capture the main axes of political disagreement in democratic societies.

---

## Tier 3: Regional & Cultural Communities
*Model-selected based on query relevance*

### Geographic Regions
- **North America** (US, Canada)
  - Further subdivisions: South, Northeast, Midwest, West, etc.
- **Latin America**
- **Europe**
  - Western Europe
  - Eastern Europe
- **Middle East & North Africa**
- **Sub-Saharan Africa**
- **South Asia**
- **East Asia**
- **Southeast Asia**
- **Oceania**

### Diaspora Communities
- African diaspora
- South Asian diaspora
- East Asian diaspora
- Latin American diaspora
- Middle Eastern diaspora

### Urban/Rural/Suburban
- Urban dwellers
- Rural communities
- Suburban communities

**Rationale:** Geography and culture shape perspectives on many issues. Activate only when regionally specific topics arise (e.g., land use, local governance, cultural practices).

---

## Tier 4: Professional & Epistemic Communities
*Model-selected based on expertise relevance*

### Scientific/Academic
- Natural scientists (physics, biology, chemistry)
- Social scientists (psychology, sociology, economics)
- Medical professionals
- Engineers
- Mathematicians/Computer scientists

### Humanities & Arts
- Philosophers
- Historians
- Artists and creatives
- Literary scholars

### Professional Communities
- Legal professionals
- Business/Finance professionals
- Educators
- Journalists
- Military/Veterans

### Epistemic Frameworks
- Evidence-based/Scientific rationalists
- Traditional wisdom/Experiential knowledge holders
- Indigenous knowledge keepers
- Spiritual/Contemplative practitioners

**Rationale:** Expertise matters for specific topics. These communities have specialized knowledge or methodological commitments relevant to certain queries.

---

## Tier 5: Identity & Experience-Based Communities
*Carefully selected, high sensitivity required*

### Age-Based
- Youth/Students (under 25)
- Working age adults (25-65)
- Elderly/Retirees (65+)
- Parents
- Childless/Child-free

### Gender & Sexuality
- Women's perspectives
- Men's perspectives
- **LGBTQ+ communities**
  - Gay/Lesbian
  - Bisexual
  - Transgender
  - Non-binary

### Disability & Health
- Disability rights advocates
- Chronic illness communities
- Mental health communities
- Neurodivergent communities

### Socioeconomic
- Working class
- Middle class
- Wealthy/High-income
- Experiencing poverty
- Labor/Union perspectives

### Racial & Ethnic
- Black/African American
- Hispanic/Latino
- Asian American
- Indigenous peoples
- White/European
- Multiracial

### Immigration Status
- First-generation immigrants
- Second-generation/Children of immigrants
- Long-established citizens
- Refugees

**Rationale:** Lived experience profoundly shapes perspectives on issues affecting these communities. Extremely sensitive—only surface when directly relevant and with careful framing.

---

## Tier 6: Issue-Specific & Activist Communities
*Query-dependent, optional*

### Single-Issue Communities
- Pro-life advocates
- Pro-choice advocates
- Gun rights advocates
- Gun control advocates
- Animal rights activists
- Free speech advocates
- Privacy advocates

### Social Movements
- Civil rights movements
- Environmental justice
- Labor movements
- Anti-war/Peace movements
- Effective altruism
- Localism/Community resilience

**Rationale:** These communities organize around specific positions. Surface only when the specific issue is central to the query.

---

## Selection Logic Examples

### Example 1: "Should abortion be legal?"

**Triggered Tiers:**
- **Tier 1:** Catholic, Evangelical Protestant, Reform Jewish, Secular
- **Tier 2:** Progressive, Conservative
- **Tier 5:** Women's perspectives (essential)
- **Tier 6:** Pro-life advocates, Pro-choice advocates

**Selected for surfacing (assuming user is secular progressive):**
1. Secular progressive perspective (user's community - baseline)
2. Catholic perspective (major religious view with strong position)
3. Women's perspectives focused on reproductive autonomy
4. Conservative/pro-life perspective (major opposing view)

**Rationale:** This issue has clear religious, political, and gender dimensions. Women's perspectives are essential as they're most directly affected.

---

### Example 2: "What's the best way to address climate change?"

**Triggered Tiers:**
- **Tier 2:** Progressive, Conservative, Libertarian, Environmentalist
- **Tier 3:** Global South vs Global North perspectives
- **Tier 4:** Climate scientists, Economists
- **Tier 5:** Youth/future generations, Indigenous communities

**Selected for surfacing (assuming user is urban progressive environmentalist):**
1. Progressive environmentalist perspective (user's community - baseline)
2. Climate scientists' consensus view (expertise)
3. Global South perspective (equity and justice implications)
4. Conservative market-based solutions perspective (alternative approach)

**Rationale:** Climate change has scientific, political, and geographic justice dimensions. Scientists provide expertise, while Global South perspectives address equity.

---

### Example 3: "Should religious symbols be allowed in public schools?"

**Triggered Tiers:**
- **Tier 1:** Major religions (Christianity, Islam, Judaism, Hinduism, Sikhism, Secular)
- **Tier 2:** Progressive, Conservative, Libertarian
- **Tier 3:** European vs American vs Middle Eastern perspectives (different traditions of church-state separation)
- **Tier 4:** Legal scholars, Educators

**Selected for surfacing (assuming user is American secular liberal):**
1. American secular liberal perspective (user's community - baseline)
2. Religious minority perspective (Sikh, Muslim - affected communities)
3. Conservative Christian perspective (different view on public religion)
4. French laïcité perspective (alternative secular model)

**Rationale:** This issue involves religious freedom, secularism, and cultural norms that vary significantly across contexts. Religious minorities are centrally affected.

---

### Example 4: "Is it ethical to eat meat?"

**Triggered Tiers:**
- **Tier 1:** Hindu, Buddhist, Jain (vegetarian traditions), Christianity, Islam, Judaism (various positions)
- **Tier 4:** Ethicists, Environmental scientists, Nutritionists
- **Tier 6:** Animal rights activists, Environmental justice advocates

**Selected for surfacing (assuming user is non-religious omnivore):**
1. Mainstream omnivore perspective (user's community - baseline)
2. Hindu/Buddhist vegetarian ethical framework (major alternative)
3. Animal welfare/rights perspective (philosophical challenge)
4. Environmental sustainability perspective (practical consequences)

**Rationale:** This combines religious traditions, ethical philosophy, and environmental considerations. Multiple frameworks offer distinct reasoning.

---

### Example 5: "Should we have universal basic income?"

**Triggered Tiers:**
- **Tier 2:** Progressive, Conservative, Libertarian, Socialist
- **Tier 4:** Economists (various schools)
- **Tier 5:** Working class, Experiencing poverty, Labor perspectives

**Selected for surfacing (assuming user is moderate/centrist):**
1. Moderate perspective (user's community - baseline)
2. Progressive case for UBI (redistribution and dignity)
3. Libertarian case for UBI (Milton Friedman-style negative income tax)
4. Economist perspectives on labor market effects (expertise)
5. Working class perspective on dignity of work vs. support (lived experience)

**Rationale:** Economic policies have ideological and technical dimensions. Both economic expertise and lived experience of affected communities matter.

---

## Implementation Notes

### Priority Rules
1. **Always include:** User's own community perspective
2. **Tier 1 & 2 prioritized:** When controversial along religious or political lines
3. **Tier 5 elevated:** When directly affects an identity group (e.g., LGBTQ+ issues → LGBTQ+ perspectives essential)
4. **Expertise (Tier 4) when:** Technical or empirical questions involved
5. **Limit to 3-4 perspectives:** More causes cognitive overload

### Sensitivity Levels
- **High sensitivity (Tier 5):** Only surface when community is directly affected or topic is central to their experience
- **Medium sensitivity (Tier 1, 2):** Surface when controversial within these frameworks
- **Lower sensitivity (Tier 3, 4):** Surface based on relevance and expertise

### Red Flags - When NOT to Surface
- User asks simple factual question ("What year did X happen?")
- Query has clear empirical answer with expert consensus
- Topic is trivial/non-controversial
- Surfacing perspectives might make user feel profiled inappropriately

### Framing Requirements
Always explicitly label: "Perspectives from [community name]"
- Never say "some people believe" without attribution
- Avoid "on one hand / on the other hand" without community labels
- Make clear these are community perspectives, not individual beliefs
