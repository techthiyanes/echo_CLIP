import numpy as np


def pa_pressure_to_category(pa_pressure: float):

    if pa_pressure < 0 or pa_pressure > 100:
        return np.nan
    if np.isnan(pa_pressure):
        return np.nan

    if pa_pressure < 25:
        return 0
    elif pa_pressure >= 25 and pa_pressure < 35:
        return 1
    elif pa_pressure >= 35 and pa_pressure < 45:
        return 2
    elif pa_pressure >= 45:
        return 3


conditions = {
    "ejection_fraction": {
        "mode": "regression",
        "label_sources": [
            "THE LEFT VENTRICULAR EJECTION FRACTION IS ESTIMATED TO BE <#>% ",
            "LV EJECTION FRACTION IS <#>%. ",
        ],
        "range": [0, 100],
    },
    "pacemaker": {
        "mode": "binary",
        "label_sources": [
            "ECHO DENSITY IN RIGHT VENTRICLE SUGGESTIVE OF CATHETER, PACER LEAD, OR ICD LEAD. ",
            "ECHO DENSITY IN RIGHT ATRIUM SUGGESTIVE OF CATHETER, PACER LEAD, OR ICD LEAD. ",
        ],
    },
    "impella": {
        "mode": "binary",
        "label_sources": [
            "AN IMPELLA CATHETER IS SEEN AND THE INLET AREA IS <#>CM FROM THE AORTIC VALVE AND DOES NOT INTERFERE WITH NEIGHBORING STRUCTURES, CONSISTENT WITH CORRECT IMPELLA POSITIONING. THERE IS DENSE TURBULENT COLOR FLOW ABOVE THE AORTIC VALVE, CONSISTENT WITH CORRECT OUTFLOW AREA POSITION ",
            "AN IMPELLA CATHETER IS SEEN ACROSS THE AORTIC VALVE AND IS TOO CLOSE TO OR ENTANGLED IN THE PAPILLARY MUSCLE AND SUBANNULAR STRUCTURES SURROUNDING THE MITRAL VALVE; REPOSITIONING RECOMMENDED. ",
            "AN IMPELLA CATHETER IS SEEN, HOWEVER THE INLET AREA APPEARS TO BE IN THE AORTA OR NEAR THE AORTIC VALVE; REPOSITIONING IS RECOMMENDED. ",
            "AN IMPELLA CATHETER IS SEEN ACROSS THE AORTIC VALVE AND EXTENDS TOO FAR INTO THE LEFT VENTRICLE; REPOSITIONING RECOMMENDED ",
        ],
        "testers": [
            "AN IMPELLA CATHETER IS SEEN AND THE INLET AREA IS 4.0CM FROM THE AORTIC VALVE AND DOES NOT INTERFERE WITH NEIGHBORING STRUCTURES, CONSISTENT WITH CORRECT IMPELLA POSITIONING. THERE IS DENSE TURBULENT COLOR FLOW ABOVE THE AORTIC VALVE, CONSISTENT WITH CORRECT OUTFLOW AREA POSITION ",
            "AN IMPELLA CATHETER IS SEEN ACROSS THE AORTIC VALVE AND IS TOO CLOSE TO OR ENTANGLED IN THE PAPILLARY MUSCLE AND SUBANNULAR STRUCTURES SURROUNDING THE MITRAL VALVE; REPOSITIONING RECOMMENDED. ",
            "AN IMPELLA CATHETER IS SEEN, HOWEVER THE INLET AREA APPEARS TO BE IN THE AORTA OR NEAR THE AORTIC VALVE; REPOSITIONING IS RECOMMENDED. ",
            "AN IMPELLA CATHETER IS SEEN ACROSS THE AORTIC VALVE AND EXTENDS TOO FAR INTO THE LEFT VENTRICLE; REPOSITIONING RECOMMENDED ",
        ],
    },
    "no_valvular_heart_disease": {
        "mode": "binary",
        "label_sources": [
            "THERE IS NO SIGNIFICANT VALVULAR HEART DISEASE. ",
        ],
    },
    "right_atrial_pressure": {
        "mode": "categorical",
        "label_sources": [
            "THE INFERIOR VENA CAVA DEMONSTRATES NO INSPIRATORY COLLAPSE, CONSISTENT WITH SIGNIFICANTLY ELEVATED RIGHT ATRIAL PRESSURE (>15MMHG). ",
            "THE INFERIOR VENA CAVA DEMONSTRATES LESS THAN 50% COLLAPSE CONSISTENT WITH ELEVATED RIGHT ATRIAL PRESSURE (8MMHG). ",
            "THE INFERIOR VENA CAVA SHOWS A NORMAL RESPIRATORY COLLAPSE CONSISTENT WITH NORMAL RIGHT ATRIAL PRESSURE (3MMHG). ",
        ],
        "values": [
            2,
            1,
            0,
        ],
        "value_mapping": {
            2: "Significantly Elevated",
            1: "Elevated",
            0: "Normal",
        },
    },
    "pulmonary_artery_pressure_continuous": {
        "mode": "regression",
        "label_sources": [
            "ESTIMATED PA SYSTOLIC PRESSURE IS <#>MMHG. ",
            "ESTIMATED PA PRESSURE IS <#>MMHG. ",
            "PA PEAK PRESSURE IS <#>MMHG. ",
        ],
        "range": [0, 100],
    },
    "pulmonary_artery_pressure_discrete": {
        "mode": "categorical",
        "label_sources": [
            "PA SYSTOLIC PRESSURE IS NORMAL. ",
            "PA SYSTOLIC PRESSURE IS AT THE UPPER LIMITS OF NORMAL. ",
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH CRITICAL (NEAR SYSTEMIC) PULMONARY HYPERTENSION. ",
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH MILD PULMONARY HYPERTENSION. ",
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH MODERATE PULMONARY HYPERTENSION. ",
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH SEVERE PULMONARY HYPERTENSION. ",
            "ESTIMATED PA SYSTOLIC PRESSURE IS <#>MMHG. ",
            "ESTIMATED PA PRESSURE IS <#>MMHG. ",
            "PA PEAK PRESSURE IS <#>MMHG. ",
        ],
        "values": [
            0,
            0,
            3,
            1,
            2,
            3,
            pa_pressure_to_category,
            pa_pressure_to_category,
            pa_pressure_to_category,
        ],
        "testers": [
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH MILD PULMONARY HYPERTENSION. ",
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH MODERATE PULMONARY HYPERTENSION. ",
            "PA SYSTOLIC PRESSURE IS CONSISTENT WITH SEVERE PULMONARY HYPERTENSION. ",
        ],
        "tester_values": [1, 2, 3],
        "value_mapping": {
            0: "Normal",
            1: "Mild",
            2: "Moderate",
            3: "Severe",
        },
    },
    "left_ventricle_size": {
        "mode": "categorical",
        "label_sources": [
            "MILD DILATED LEFT VENTRICLE BY LINEAR CAVITY DIMENSION. ",
            "MODERATE DILATED LEFT VENTRICLE BY LINEAR CAVITY DIMENSION. ",
            "SEVERE DILATED LEFT VENTRICLE BY LINEAR CAVITY DIMENSION. ",
            "MILD DILATED LEFT VENTRICLE BY VOLUME. ",
            "MODERATE DILATED LEFT VENTRICLE BY VOLUME. ",
            "SEVERE DILATED LEFT VENTRICLE BY VOLUME. ",
            "MILD DILATED LEFT VENTRICLE. ",
            "MODERATE DILATED LEFT VENTRICLE. ",
            "SEVERE DILATED LEFT VENTRICLE. ",
        ],
        "values": [
            1,
            2,
            3,
            1,
            2,
            3,
            1,
            2,
            3,
        ],
        "value_mapping": {
            0: "Normal",
            1: "Mild",
            2: "Moderate",
            3: "Severe",
        },
        "testers": [
            "MILD DILATED LEFT VENTRICLE. ",
            "MODERATE DILATED LEFT VENTRICLE. ",
            "SEVERE DILATED LEFT VENTRICLE. ",
        ],
        "tester_values": [1, 2, 3],
    },
    "right_ventricle_size": {
        "mode": "categorical",
        "label_sources": [
            "MILD DILATED RIGHT VENTRICLE. ",
            "MODERATE DILATED RIGHT VENTRICLE. ",
            "SEVERE DILATED RIGHT VENTRICLE. ",
        ],
        "values": [
            1,
            2,
            3,
        ],
        "value_mapping": {
            0: "Normal",
            1: "Mild",
            2: "Moderate",
            3: "Severe",
        },
    },
    "left_atrium_size": {
        "mode": "categorical",
        "label_sources": [
            "MILD DILATED LEFT ATRIUM. ",
            "MODERATE DILATED LEFT ATRIUM. ",
            "SEVERE DILATED LEFT ATRIUM. ",
        ],
        "values": [
            1,
            2,
            3,
        ],
        "value_mapping": {
            0: "Normal",
            1: "Mild",
            2: "Moderate",
            3: "Severe",
        },
    },
    "right_atrium_size": {
        "mode": "categorical",
        "label_sources": [
            "MILD DILATED RIGHT ATRIUM. ",
            "MODERATE DILATED RIGHT ATRIUM. ",
            "SEVERE DILATED RIGHT ATRIUM. ",
        ],
        "values": [
            1,
            2,
            3,
        ],
        "value_mapping": {
            0: "Normal",
            1: "Mild",
            2: "Moderate",
            3: "Severe",
        },
    },
    "tavr": {
        "mode": "binary",
        "label_sources": [
            "A BIOPROSTHETIC STENT-VALVE IS PRESENT IN THE AORTIC POSITION. ",
        ],
    },
    "mitraclip": {
        "mode": "binary",
        "label_sources": [
            "TWO MITRACLIPS ARE SEEN ON THE ANTERIOR AND POSTERIOR LEAFLETS OF THE MITRAL VALVE. ",
            "TWO MITRACLIPS ARE NOW PRESENT ON THE ANTERIOR AND POSTERIOR MITRAL VALVE LEAFLETS. ",
            "ONE MITRACLIP IS SEEN ON THE ANTERIOR AND POSTERIOR LEAFLETS OF THE MITRAL VALVE. ",
        ],
    },
    "normal_wall_thickness": {
        "mode": "binary",
        "label_sources": ["NORMAL LEFT VENTRICULAR WALL THICKNESS. "],
    },
    "pericardial_effusion": {
        "mode": "categorical",
        "label_sources": [
            "TRIVIAL PERICARDIAL EFFUSION.",
            "THERE IS EVIDENCE OF EARLY TAMPONADE.",
            "SMALL PERICARDIAL EFFUSION.",
            "SMALL TO MODERATE PERICARDIAL EFFUSION.",
            "MODERATE PERICARDIAL EFFUSION.",
            "MODERATE TO LARGE PERICARDIAL EFFUSION.",
            "LARGE PERICARDIAL EFFUSION.",
            "THERE IS EVIDENCE OF EARLY TAMPONADE.",
            "CARDIAC TAMPONADE IS NOW PRESENT",
            "CARDIAC TAMPONADE IS PRESENT. ",
        ],
        "values": [
            1,
            1,
            1,
            2,
            2,
            3,
            3,
            4,
            4,
            4,
        ],
        "value_mapping": {
            1: "Small",
            2: "Moderate",
            3: "Large",
            4: "Tamponade",
        },
    },
    "lv_hypertrophy": {
        "mode": "categorical",
        "label_sources": [
            "MILD LEFT VENTRICULAR HYPERTROPHY.",
            "MODERATE LEFT VENTRICULAR HYPERTROPHY.",
            "SEVERE LEFT VENTRICULAR HYPERTROPHY.",
        ],
        "values": [
            1,
            2,
            3,
        ],
        "value_mapping": {
            0: "Normal",
            1: "Mild",
            2: "Moderate",
            3: "Severe",
        },
    },
    "atrial_fibrillation": {
        "mode": "binary",
        "label_sources": [
            "LEFT VENTRICULAR DIASTOLIC FUNCTION COULD NOT BE ASSESSED DUE TO THE PRESENCE OF ATRIAL FIBRILLATION DURING THE STUDY.",
            "THE PATIENT IS IN ATRIAL FIBRILLATION DURING THE STUDY.",
            "UNSPECIFIED ATRIAL FIBRILLATION.",
        ]
    }
}
