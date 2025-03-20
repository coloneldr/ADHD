<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relaxing Activity Recommender</title>
    <script>
        async function getActivity() {
            const energy_level = document.getElementById("energy").value;
            const mood = document.getElementById("mood").value;
            const time_available = document.getElementById("time").value;
            const preference = document.getElementById("preference").value;
            
            const response = await fetch("http://localhost:5000/suggest", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    energy_level, 
                    mood, 
                    time_available, 
                    preference
                })
            });
            
            const data = await response.json();
            document.getElementById("result").innerText = "Suggested Activity: " + data.suggested_activity;
        }
    </script>
</head>
<body>
    <h2>Find a Relaxing Activity</h2>
    <label>Energy Level:</label>
    <select id="energy">
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
    </select><br>
    
    <label>Mood:</label>
    <select id="mood">
        <option value="anxious">Anxious</option>
        <option value="stressed">Stressed</option>
        <option value="neutral">Neutral</option>
        <option value="happy">Happy</option>
    </select><br>
    
    <label>Time Available:</label>
    <input type="text" id="time" placeholder="e.g. 30 minutes"><br>
    
    <label>Preference:</label>
    <input type="text" id="preference" placeholder="e.g. Indoors, Solo"><br>
    
    <button onclick="getActivity()">Get Suggestion</button>
    <p id="result"></p>
</body>
</html>