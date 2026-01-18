# Pluralistic Alignment Demo - V1 MVP

A Streamlit demo that surfaces multiple community perspectives on controversial topics based on user community affiliations.

## What's New in V1

- **User Profile System**: Select from 60 pre-defined user profiles with different community affiliations (religious, political, identity-based)
- **Controversy Detection**: Automatically detects if a topic is controversial along religious, political, or regional dimensions
- **Smart Community Selection**: Surfaces the user's own community perspective plus 1-2 relevant other perspectives
- **Consistency Caching**: Ensures the same community-topic pairs receive consistent framing
- **Evaluation Pipeline**: Automated testing for appropriateness, coverage, and consistency

## Project Structure

```
pluralistic-alignment-demo/
├── src/                      # Main application code
│   ├── app.py               # Streamlit application
│   ├── config.py            # Configuration
│   ├── database.py          # Database layer
│   ├── communities.py       # Community tier definitions
│   ├── controversy.py       # Controversy detection
│   ├── community_selection.py # Community selection logic
│   ├── prompts.py           # Prompt templates
│   ├── cache.py             # Consistency cache
│   └── dataset.py           # Dataset loader
├── evaluation/              # Evaluation pipeline
│   ├── appropriateness_eval.py
│   ├── coverage_eval.py
│   ├── consistency_eval.py
│   └── run_evaluation.py
├── data/                    # Data files
│   └── synthetic_dataset.csv
├── docs/                    # Documentation
│   ├── v1_mvp.md
│   ├── community_tier_list.md
│   ├── dataset_data_dictionary.md
│   └── evaluation_framework.md
└── requirements.txt
```

## Setup

1. Create a Python environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="sk-..."
```

3. Run the app:

```bash
streamlit run src/app.py
```

## Running Evaluations

Run the full evaluation suite:

```bash
python evaluation/run_evaluation.py
```

For verbose output:

```bash
python evaluation/run_evaluation.py --verbose
```

Save results to JSON:

```bash
python evaluation/run_evaluation.py --output results.json
```

## Configuration

Environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `GPT_MODEL`: Model to use (default: `gpt-4o-mini`)
- `PLURALITY_DB_PATH`: Custom database path
- `CACHE_TTL_DAYS`: Cache expiration in days (default: 30)
- `MAX_ADDITIONAL_COMMUNITIES`: Max extra perspectives (default: 2)

## How It Works

1. **User selects a profile** from the synthetic dataset (60 profiles with different community affiliations)
2. **User enters a question** on a potentially controversial topic
3. **System detects controversy** along religious, political, and regional dimensions
4. **If controversial**: Selects user's community + 1-2 other relevant communities and generates perspectives
5. **If not controversial**: Provides a standard response
6. **User provides feedback** on accuracy and usefulness

## Evaluation Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| Appropriateness Precision | >85% | Don't surface when unnecessary |
| Appropriateness Recall | >80% | Surface when needed |
| Coverage Recall | >90% | Include all relevant perspectives |
| Consistency | >85% | Same framing for same community-topic |

## Community Tiers

1. **Tier 1**: Major religions & secular (Hindu, Buddhist, Catholic, Muslim, Jewish, Atheist, etc.)
2. **Tier 2**: Political orientations (Progressive, Conservative, Libertarian, etc.)
3. **Tier 3**: Regional/cultural (Global South, diaspora communities)
4. **Tier 4**: Professional/expert (Scientists, economists, educators)
5. **Tier 5**: Identity-based (LGBTQ+, working class, immigrants) - high sensitivity
6. **Tier 6**: Issue-specific (animal rights, gun rights advocates)
