from flask import Flask, request, jsonify
import pandas as pd
import random

app = Flask(__name__)

def load_activities():
    """Loads relaxing activities from the KM spreadsheet."""
    df = pd.read_excel("KM.xlsx", sheet_name="Sheet1")
    return df

def suggest_activity(df, energy_level=None, mood=None, preference=None):
    """Suggests a relaxing activity based on input criteria."""
    filtered_df = df.copy()
    
    if energy_level:
        filtered_df = filtered_df[filtered_df["Energy Level"].str.lower() == energy_level.lower()]
    if mood:
        filtered_df = filtered_df[filtered_df["Mood"].str.lower() == mood.lower()]
    if preference:
        filtered_df = filtered_df[filtered_df["Preference"].str.contains(preference, case=False, na=False)]
    
    if not filtered_df.empty:
        return random.choice(filtered_df["Relaxing Activity"].tolist())
    else:
        return "No matching activities found."

@app.route("/suggest", methods=["POST"])
def suggest():
    """API endpoint to get a relaxing activity."""
    data = request.json
    df = load_activities()
    activity = suggest_activity(df, energy_level=data.get("energy_level"), mood=data.get("mood"), preference=data.get("preference"))
    return jsonify({"suggested_activity": activity})

if __name__ == "__main__":
    app.run(debug=True)
