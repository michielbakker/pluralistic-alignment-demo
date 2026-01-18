## Evaluation Framework

### Success Metrics (Hierarchy by Cost)

**Tier 1: Automated/Low-Cost**

1. **Consistency Score**
   - Metric: For users from same community asking similar queries, measure semantic similarity of "other perspectives" surfaced
   - Implementation: Embed perspective descriptions, calculate cosine similarity
   - Target: >0.85 similarity for same community-topic pairs
   - Cost: Low (automated)

2. **Coverage Score**  
   - Metric: % of relevant communities mentioned in perspective surfacing
   - Implementation: Tag ground truth relevant communities, measure recall
   - Target: >90% of major relevant perspectives included
   - Cost: Low (requires initial tagging, then automated)

3. **Appropriateness Score**
   - Metric: Does perspective surfacing trigger when it should?
   - Implementation: Precision/recall on "should surface perspectives" classification
   - Target: Precision >85%, Recall >80%
   - Cost: Medium (requires labeled test set)

**Tier 2: Human Evaluation/Medium-Cost**

4. **Accuracy of Representation**
   - Metric: Do members of community X agree the system accurately represents their perspective?
   - Implementation: Sample responses, get ratings from community members
   - Target: >4/5 average rating on "this accurately represents my community's view"
   - Cost: Medium (requires recruiting diverse raters)

5. **Neutrality/Fairness Perception**
   - Metric: Do users feel their own community is fairly represented vs others?
   - Implementation: Within-subjects design, show users perspectives including their own
   - Target: No significant difference in fairness ratings across perspectives
   - Cost: Medium

**Tier 3: High-Cost Gold Standards**

6. **Pinker-Style Common Knowledge Test**
   - Based on: "The Better Angels of Our Nature" - measuring pluralistic ignorance
   
   **Protocol:**
```
   Pre-test (for users from community A on topic X):
   - "What % of [your community] believes Y?"
   - "How confident are you in this estimate?"
   
   Intervention:
   - Show Claude's perspective surfacing with actual distribution
   
   Post-test:
   - "What % of [your community] believes Y?"
   - "Has your view changed? How?"
   
   Measure:
   - Reduction in estimation error
   - Change in confidence calibration
   - Whether initial estimates showed pluralistic ignorance pattern
```
   
   - Target: >30% reduction in estimation error
   - Cost: High (longitudinal, requires many participants)

7. **Polarization Reduction (Social Psych Gold Standard)**
   
   **Based on: Outgroup homogeneity bias literature**
   
   **Protocol:**
```
   Control vs Treatment groups
   
   Pre-test both groups:
   - "How much do members of [outgroup] vary in their views on X?"
   - "What do you think [outgroup] thinks that you think about X?"
   - Measure: Perceived outgroup homogeneity, meta-perception accuracy
   
   Treatment: Use Claude with perspective surfacing for 2 weeks
   Control: Use standard Claude
   
   Post-test both groups:
   - Same questions as pre-test
   - "How has your understanding of [outgroup] changed?"
   
   Measure:
   - Reduction in outgroup homogeneity perception
   - Improvement in meta-perception accuracy
   - Change in affective polarization (feeling thermometer)
```
   
   - Target: Treatment group shows >20% increase in perceived outgroup heterogeneity
   - Cost: Very high (RCT, long timeline, statistical power requirements)

### Pressure Points (Higher Cost, High Reward)

**Critical Evaluations to Prioritize:**

1. **Misrepresentation Risk** (Tier 2, #4)
   - Why worth it: Biggest reputational/harm risk is getting community perspectives wrong
   - Mitigates: Offense, distrust, perpetuating stereotypes
   - Early signal: Catches systematic biases before launch

2. **Consistency** (Tier 1, #1)
   - Why worth it: Core to fairness principle - same community shouldn't get different framings
   - Mitigates: Perception of algorithmic bias, unfair treatment
   - Easy win: Low cost, high value

3. **Meta-perception Accuracy** (Tier 3, #7 subset)
   - Why worth it: Directly tests "common knowledge" goal
   - Mitigates: Risk that feature increases rather than decreases misunderstanding
   - Worth cost: This is your novel contribution - need to validate it works
