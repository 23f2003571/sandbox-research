# IFID Data Entry Guidelines

## Core Principle
**NEVER take CSV entries as ground truth.** All source files are noisy temporaries. We extract only clean signals and normalize them according to these rules.

---

## Controlled Vocabularies

All valid enum values are defined in `enums.py`:
- **TYPES**: plant, dairy, animal, marine, fungal, microbial, synthetic
- **MATTER_STATES**: powder, coarse_grits, flakes, etc.
- **PROCESSING_METHODS**: milling, fermentation, drying, etc.

**You cannot modify `enums.py` directly.** If you need a new enum value:
1. Add a request to `enum_requests.md` with: what enum, the value, why it's needed
2. Wait for review and approval
3. The value will be merged into `enums.py` after approval

---

## Validation

**Before committing, run the lint script:**
```bash
python lint.py
```

This validates your db.py against:
- All enum values in enums.py
- Naming conventions in ENTRY_GUIDELINES.md
- Data type requirements

If lint passes, you're safe to commit.

---

## Naming & ID Conventions

### Source Names
- Use lowercase, space-separated (e.g., "bansi wheat", "wheat")

### Form IDs
- **Direction**: generic → specific (e.g., `wheat_flakes`, `wheat_malted`)
- NOT: `malted_wheat`, `flakes_wheat`, `semolina_wheat`
- Use lowercase with underscores
- Compound modifiers joined with hyphens in the id if multi-word (e.g., `wheat_pre-cooked`)

### Processing Methods
- List items in lowercase
- Multi-word methods use hyphens (e.g., `"pre-cooking"`, NOT `"precooking"`)
- Empty list `[]` if processing method is unclear or absent—**never approximate or assume**

---

## Entity Fields

### Source
```python
Source(
    name: str,           # lowercase, space-separated
    type: str,           # "grain", "mineral", "synthetic", etc. (NOT raw names from CSV)
    is_allergen: bool,   # well-documented allergen status only
    is_declarable: bool  # regulatory declarability
)
```

- **type**: Normalize from CSV. E.g., "raw_agricultural_material" → "grain"
- Only values we can clearly justify from data

### IngredientForm
```python
IngredientForm(
    id: str,             # generic -> specific (e.g., "wheat_flakes")
    matter_state: str    # "powder", "coarse_grits", "flakes", etc.
)
```

---

## Relationships

### FormOf
A Source or IngredientForm can become another IngredientForm through processing.

**Rule**: Only add if:
1. We have explicit evidence in the CSV (or domain knowledge)
2. The processing method is known or can be left empty
3. We are NOT inferring hypothetical forms

**Example of what NOT to do:**
- CSV has `wheat → flour (milling)` and `wheat → malted_wheat (fermentation)`
- Do NOT infer `bansi_wheat → malted_wheat` just because bansi_wheat is a wheat variety
- Only add `bansi_wheat → bansi_semolina` if we see evidence of that specific form

### VarietyOf
A Source can be a variety of another Source.

**Rule**: Only add if explicitly clear in the data that one is a variety/cultivar of another.

**Example:**
- `bansi_wheat` is a variety of `wheat` → add `VarietyOf(base=wheat, variety=bansi_wheat)`

---

## Data Extraction Rules

1. **Ignore incomplete rows**: If a row has NULL, "?", or ambiguous values in key fields, skip it
2. **Normalize types**: Map CSV type strings to our controlled vocabulary (grain, mineral, synthetic, etc.)
3. **Never assume relationships**: Only add what we have evidence for
4. **Empty processing methods**: If processing is unclear, use `[]` rather than guessing
5. **No hypothetical entries**: We add wheat_malted only if we see wheat being malted in our dataset; we don't add bansi_malted "just in case"

---

## Checklist Before Adding an Entry

- [ ] Is this a clear signal or extracting noise from the CSV?
- [ ] Are all required fields (name, type, form id) well-defined?
- [ ] Do I have evidence for each relationship I'm adding?
- [ ] Are processing methods known, or am I leaving them empty?
- [ ] Are my IDs following generic → specific order?
- [ ] Am I using hyphens for multi-word processing methods?
- [ ] Did I normalize type from the CSV raw value to our controlled vocabulary?
