import pandas as pd
from pipeline import HeartPipeline

hp = HeartPipeline.load()

sample = pd.DataFrame([{
    'age': 58,
    'resting_blood_pressure': 130,
    'serum_cholesterol_mg_per_dl': 240,
    'max_heart_rate_achieved': 145,
    'oldpeak_eq_st_depression': 2.2,
    'sex': 1,
    'chest_pain_type': 3,
    'exercise_induced_angina': 1,
    'slope_of_peak_exercise_st_segment': 2,
    'fasting_blood_sugar_gt_120_mg_per_dl': 0,
    'resting_ekg_results': 1,
    'num_major_vessels': 0,
    'thal': 2
}])

print("Risk Probability:", hp.predict_proba(sample)[0][1])
