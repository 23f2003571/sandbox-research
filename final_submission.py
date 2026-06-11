# IFID Data Analysis Task
# submission.py
# Generated from final worksheet.
# Duplicates are collapsed. Flagged rows are listed at the end.

import sys
import os

# Adds 'D:\PyDB' to the search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from db import Database, Source, IngredientForm, FormOf, VarietyOf

db = Database()
# Sources

milk = db.add(Source(
    name="milk",
    type="dairy",
    is_allergen=True,
    is_declarable=True
))

whey = db.add(Source(
    name="whey",
    type="dairy",
    is_allergen=True,
    is_declarable=True
)) # Unless it is a natural source with no artificial processing, it cannot be a source. If this is because you want to have whey powder being form of whey etc,..then you can just create whey as an IngredientForm and relate it to milk as a form of milk. Then create whey powder as a form of IngredientForm whey.

# Look up to see if 'whey' alone is a sufficient enough label in food products by FSSAI rules, if fssai says or expects more detailed form like whey protein isolate, that would mean brands can't just choose 'whey' as an option. So in that case mark is_declarable=False for whey.

# This is how is_declarable comes into play. milk(Source) is is_declarable=False while cow_milk(Source) is is_declarable=True. This is because milk is a broad category that can encompass various forms and sources, while cow milk is a specific source that can be declared on food labels. If whey is not considered a specific source that can be declared on labels, then it should be marked as is_declarable=False, so if you come across any ingredient such that it isn't a specific source that can be declared on labels, then you can mark it as is_declarable=False.

# Your thumb of rule would be - can a brand declare this ingredient on a label as it is, if not mark is_declarable=False.


cow_milk = db.add(Source(
    name="cow milk",
    type="dairy",
    is_allergen=True,
    is_declarable=True
))

db.relate(VarietyOf(base=milk, variety=cow_milk))


# Forms of milk

whey_form = db.add(IngredientForm(id="whey", matter_state="liquid")) #why is whey added as both a form and source? ToAnswer
db.relate(FormOf(origin=milk, form=whey_form, processing_method=["coagulation"]))

curd = db.add(IngredientForm(id="curd", matter_state="fermented_dairy"))
db.relate(FormOf(origin=milk, form=curd, processing_method=["fermentation"]))

dahi = db.add(IngredientForm(id="dahi", matter_state="fermented_dairy"))
db.relate(FormOf(origin=milk, form=dahi, processing_method=["fermentation"])) #dahi=curd, so it must not be added again when curd is already added.

# Rule of thumb:
# If it's a synonymn of the same ingredient, then don't add a new entry.
# If it's different, you can add a new entry. But after entering if both it's entries look the same, then question if they are actually different or not. If it's for sure different, then think of why is the current entry failing to capture the difference and where to add that.

ghee = db.add(IngredientForm(id="ghee", matter_state="clarified_fat"))
db.relate(FormOf(origin=milk, form=ghee, processing_method=["clarification"]))

cream = db.add(IngredientForm(id="cream", matter_state="cream"))
db.relate(FormOf(origin=milk, form=cream, processing_method=["separation"]))

butter = db.add(IngredientForm(id="butter", matter_state="fat"))
db.relate(FormOf(origin=milk, form=butter, processing_method=["churning"]))

cheese = db.add(IngredientForm(id="cheese", matter_state="cheese"))
db.relate(FormOf(origin=milk, form=cheese, processing_method=["coagulation"]))

paneer = db.add(IngredientForm(id="paneer", matter_state="cheese"))
db.relate(FormOf(origin=milk, form=paneer, processing_method=["coagulation"])) # Whys is the matter state here cheese? ToAnswer.

yogurt = db.add(IngredientForm(id="yogurt", matter_state="fermented_dairy"))
db.relate(FormOf(origin=milk, form=yogurt, processing_method=["fermentation"]))

casein = db.add(IngredientForm(id="casein", matter_state="protein"))
db.relate(FormOf(origin=milk, form=casein, processing_method=["coagulation"]))

yoghurt = db.add(IngredientForm(id="yoghurt", matter_state="fermented_dairy"))
db.relate(FormOf(origin=milk, form=yoghurt, processing_method=["fermentation"])) # yoghurt and yogurt are the same, so it must not be added again when yogurt is already added.

lactose = db.add(IngredientForm(id="lactose", matter_state="sugar"))
db.relate(FormOf(origin=milk, form=lactose, processing_method=["separation"])) #Why is the matter state sugar here? ToAnswer

raw_milk = db.add(IngredientForm(id="raw_milk", matter_state="liquid"))
db.relate(FormOf(origin=milk, form=raw_milk, processing_method=[])) # What is raw milk and how is it different from milk? What's the reason there's no processing method?

milk_fat = db.add(IngredientForm(id="milk_fat", matter_state="fat"))
db.relate(FormOf(origin=milk, form=milk_fat, processing_method=["centrifugation"]))

toned_milk = db.add(IngredientForm(id="toned_milk", matter_state="liquid")) #Use generic_specific rule. So the ID must be milk_toned.
db.relate(FormOf(origin=milk, form=toned_milk, processing_method=["standardization"]))

milk_powder = db.add(IngredientForm(id="milk_powder", matter_state="powder"))
db.relate(FormOf(origin=milk, form=milk_powder, processing_method=["drying"]))

milk_solids = db.add(IngredientForm(id="milk_solids", matter_state="solid"))
db.relate(FormOf(origin=milk, form=milk_solids, processing_method=["concentration"]))

skimmed_milk = db.add(IngredientForm(id="skimmed_milk", matter_state="liquid")) #milk_skimmed
db.relate(FormOf(origin=milk, form=skimmed_milk, processing_method=["skimming"]))

milk_protein = db.add(IngredientForm(id="milk_protein", matter_state="protein"))
db.relate(FormOf(origin=milk, form=milk_protein, processing_method=["coagulation"]))

cottage_cheese = db.add(IngredientForm(id="cottage_cheese", matter_state="cheese")) # Why is the matter state cheese here? If you meant to convey as it's a variety of cheese, then you can use the variety_of relationship to relate it to cheese. 
db.relate(FormOf(origin=milk, form=cottage_cheese, processing_method=["coagulation"])) 

condensed_milk = db.add(IngredientForm(id="condensed_milk", matter_state="concentrate"))
db.relate(FormOf(origin=milk, form=condensed_milk, processing_method=["condensation"]))

full_cream_milk = db.add(IngredientForm(id="full_cream_milk", matter_state="liquid"))
db.relate(FormOf(origin=milk, form=full_cream_milk, processing_method=["standardization"]))

dried_whole_milk = db.add(IngredientForm(id="dried_whole_milk", matter_state="powder"))
db.relate(FormOf(origin=milk, form=dried_whole_milk, processing_method=["spray-drying"]))

pasteurized_milk = db.add(IngredientForm(id="pasteurized_milk", matter_state="liquid"))
db.relate(FormOf(origin=milk, form=pasteurized_milk, processing_method=["pasteurization"]))

clarified_butter = db.add(IngredientForm(id="clarified_butter", matter_state="clarified_fat")) #How is clarified butter different from ghee? ToAnswer.
db.relate(FormOf(origin=milk, form=clarified_butter, processing_method=["clarification"]))

whole_milk_powder = db.add(IngredientForm(id="whole_milk_powder", matter_state="powder"))
db.relate(FormOf(origin=milk, form=whole_milk_powder, processing_method=["drying"]))

double_toned_milk = db.add(IngredientForm(id="double_toned_milk", matter_state="liquid"))
db.relate(FormOf(origin=milk, form=double_toned_milk, processing_method=["standardization"]))

dried_skimmed_milk = db.add(IngredientForm(id="dried_skimmed_milk", matter_state="powder"))
db.relate(FormOf(origin=milk, form=dried_skimmed_milk, processing_method=["drying"]))

skimmed_milk_powder = db.add(IngredientForm(id="skimmed_milk_powder", matter_state="powder"))
db.relate(FormOf(origin=milk, form=skimmed_milk_powder, processing_method=["skimming", "drying"])) #Great job, this is how you nest processing methods to capture the sequence of processing steps.

concentrated_milk_solids = db.add(IngredientForm(id="concentrated_milk_solids", matter_state="concentrate"))
db.relate(FormOf(origin=milk, form=concentrated_milk_solids, processing_method=["centrifugation"]))


# Forms of whey

whey_powder = db.add(IngredientForm(id="whey_powder", matter_state="powder"))
db.relate(FormOf(origin=whey, form=whey_powder, processing_method=["drying"])) #`form=` is generic and should be source agnostic. See what examples for different forms used there as an example of how this could be structured. 

whey_protein = db.add(IngredientForm(id="whey_protein", matter_state="protein"))
db.relate(FormOf(origin=whey, form=whey_protein, processing_method=["coagulation"]))

whey_protein_concentrate = db.add(IngredientForm(id="whey_protein_concentrate", matter_state="protein_concentrate"))
db.relate(FormOf(origin=whey, form=whey_protein_concentrate, processing_method=["coagulation"]))


# COLLAPSED / DUPLICATES
# "milk" — duplicate label string, source added once
# "cheese" — duplicate label string, form added once
# "yogurt" — duplicate label string, form added once
# "yoghurt" — duplicate label string, form added once
# "cow milk" — duplicate label string, source added once


# SKIPPED
# "live bacteria culture" — microbial culture; flagged because it does not fit cleanly into the current dairy source/form mapping
# "active lactic cultures" — microbial culture; flagged because it does not fit cleanly into the current dairy source/form mapping
