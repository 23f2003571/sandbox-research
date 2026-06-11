from index import Database, Source, IngredientForm, FormOf, VarietyOf

db = Database()

# Sources
wheat = db.add(Source(
    name="wheat",
    type="plant",
    is_allergen=True,
    is_declarable=True
))

flour = db.add(IngredientForm(id="flour", matter_state="flour"))
db.relate(FormOf(origin=wheat, form=flour, processing_method=["milling-whole"]))
db.relate(FormOf(origin=wheat, form=flour, processing_method=["milling-refined"]))

flour_malted = db.add(IngredientForm(id="flour_malted", matter_state="powder"))
db.relate(FormOf(origin=wheat, form=flour_malted, processing_method=["malting"]))

flakes = db.add(IngredientForm(id="flakes", matter_state="flakes"))
db.relate(FormOf(origin=wheat, form=flakes, processing_method=["flaking"]))

semolina = db.add(IngredientForm(id="semolina", matter_state="coarse_grits"))
db.relate(FormOf(origin=wheat, form=semolina, processing_method=["milling-coarse"]))


bansi_wheat = db.add(Source(
    name="bansi wheat",
    type="plant",
    is_allergen=True,
    is_declarable=True
))

db.relate(VarietyOf(base=wheat, variety=bansi_wheat))
db.relate(FormOf(origin=bansi_wheat, form=semolina, processing_method=["milling-coarse"]))

print(db)
