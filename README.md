# Awzān: Comprehensive Dataset for Arabic Poetic Meter Patterns

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Awzan/main/images/AwzanLogo.png" width = "200px"/>
 </p>

## Table of Contents
- [Summary](#summary)
- [Value of the Data](#value-of-the-data)
- [Data Description](#data-description)
- [Sample Output](#sample-output)
- [Methodology](#methodology)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Summary
Awzān is a groundbreaking dataset designed to provide a solution space for all metrical patterns (taf'ilat) of classical Arabic poetic meters. These patterns are critical for measuring the quality of Arabic poetry, as deviations from these patterns are considered structural flaws. Despite recent advancements in Arabic poetic meter research, existing studies often lack detailed taf'ilat patterns and primarily focus on identifying main meters. Awzān addresses this gap by providing fine-grained, detailed data on meter patterns.

The dataset is suitable for training large-scale models for complex tasks related to Arabic poetry, including advanced prosody analysis, meter pattern recognition, and poetic evaluation.

---

## Value of the Data
- **Overcoming limitations in large language models**: Current models struggle with Arabic prosody tasks. The dataset provides highly accurate data to enable better performance in these complex tasks.
- **Standard for meter-related research**: Awzān can serve as a benchmark for studies in meter classification and detailed taf'ilat pattern recognition.
- **Filling gaps in poetic research**: Meter pattern recognition and rhyme rule enforcement have seen limited exploration. This dataset can catalyze research in these areas.
- **Automating complex processes**: The dataset enables automation of traditionally manual processes involved in Arabic poetry analysis.
- **Unique contribution**: As far as we know, no other dataset comprehensively covers taf'ilat patterns and rhyme rules for classical Arabic poetry.

---

## Data Description
The Awzān dataset was designed to encapsulate all facets of the metrical system of classical Arabic poetry, following the rules of traditional Arabic prosody. Here’s a breakdown of the data components:

1. **Poetic Verses**
   - Verses are available in three states: partially diacritized, fully diacritized, and non-diacritized.
   - Full diacritization was achieved using a specialized diacritization model.

2. **Metrical Writing (Al-Kitabah Al-'Arudiyyah)**
   - Following the prosodic rule, all pronounced letters are written, and unpronounced ones are omitted. 
   - This was achieved using a two-phase process: a knowledge-based system to apply prosodic rules, followed by manual verification.

3. **Metrical Patterns (Al-Buhur)**
   - Main meters: categorized into 16 distinct patterns.
   - Sub-meters: divided into 4 categories (full, truncated, bisected, exhausted), depending on the number of taf'ilat in each verse.
   - Final taf'ila patterning (Darb): an additional classification based on the final taf'ila in the first hemistich of the verse.

4. **Taf'ilat Patterns**
   - **Segmented Words**: Each poetic verse is segmented into words, matching corresponding taf'ilat patterns.
   - **Binary Patterning**: Taf'ilat are represented using binary encoding, where '0' denotes a silent letter and '1' a vowel.
   - **Traditional Taf'ilat Names**: Each binary-encoded segment is mapped to a corresponding traditional taf'ilat.
   - **Modifications (Zihafat and 'Illal)**: The dataset includes permissible modifications that occur in taf'ilat patterns, categorized into zihafat (minor alterations) and 'illal (major alterations).

5. **Rhyme Data**
   - **Rhyme Type**
   - **Rhyme Letters**
   - **Rhyme Movements**
   - **Rhyme Boundaries**

---

## Sample Output
Here’s a sample of how the data is structured:

| Verse (Partially Diacritized) | Verse (Fully Diacritized) | Metrical Writing | Metrical Pattern | Taf'ilat (Binary) | Taf'ilat (Traditional) | Zihafat | 'Illal | Rhyme | Rhyme Type |
|-------------------------------|---------------------------|------------------|------------------|-------------------|------------------------|---------|--------|-------|------------|
| Al-Bayt Al-Sha'ri 1            | البيت الشعري ١            | -                | -                | 1010101010        | Fa'ulun Maf'ulun       | -       | -      | -     | -          |
| Al-Bayt Al-Sha'ri 2            | البيت الشعري ٢            | -                | -                | 0101010101        | Mustaf'ilun Fa'ilatun  | -       | -      | -     | -          |

---

## Methodology
The dataset was built using a multi-phase process:
1. **Data Selection**: The initial data were sourced from the Diwan dataset, including thousands of Arabic poetic verses.
2. **Frahidi System**: The Frahidi system was used to automatically extract all relevant prosodic features from the verses, including taf'ilat, rhyme patterns, and metrical writing.
3. **Database Construction**: The extracted data was compiled into the Awzān dataset, ensuring a complete solution space for all Arabic poetic meters.
4. **Verification and Evaluation**: Expert linguists manually verified the data to ensure accuracy and completeness.

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Awzan/main/images/AwzanMethodology.png" width = "400px"/>
 </p>

---

## Usage
The Awzān dataset can be used for:
- Training and fine-tuning machine learning models for Arabic poetry analysis.
- Developing tools for meter and rhyme pattern recognition in classical Arabic poetry.
- Advancing research in Arabic prosody, poetic metrics, and NLP applications for the Arabic language.

### Example Usage:
```python
import Awzān

# Load dataset
data = Awzān.load_data('path/to/Awzān.csv')

# Explore a sample
print(data.head())
