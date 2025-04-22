from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Star Rail character database with wiki links
search_data = {
    "Acheron": ["5★ Lightning Path: The Nihility", "The Demon of Desire", "Mysterious figure from Penacony | Wiki: https://honkai-star-rail.fandom.com/wiki/Acheron"],
    "Argenti": ["5★ Physical Path: The Erudition", "Knight of Beauty from Penacony", "Member of the Knights of Beauty | Wiki: https://honkai-star-rail.fandom.com/wiki/Argenti"],
    "Arlan": ["4★ Lightning Path: The Destruction", "Security Guard at the Herta Space Station", "Former soldier with cybernetic enhancements | Wiki: https://honkai-star-rail.fandom.com/wiki/Arlan"],
    "Asta": ["4★ Fire Path: The Harmony", "Genius researcher at the Herta Space Station", "Expert in space station operations | Wiki: https://honkai-star-rail.fandom.com/wiki/Asta"],
    "Aventurine": ["5★ Imaginary Path: The Preservation", "Chief of the Observation Unit", "Guardian of the Fragmentum | Wiki: https://honkai-star-rail.fandom.com/wiki/Aventurine"],
    "Bailu": ["5★ Lightning Path: The Abundance", "Divine Healer of the Vidyadhara", "Young but skilled doctor | Wiki: https://honkai-star-rail.fandom.com/wiki/Bailu"],
    "Black Swan": ["5★ Wind Path: The Nihility", "Enigmatic Opera Singer", "Mysterious performer from Penacony | Wiki: https://honkai-star-rail.fandom.com/wiki/Black_Swan"],
    "Blade": ["5★ Wind Path: The Destruction", "Member of the Stellaron Hunters", "Mysterious swordsman seeking revenge | Wiki: https://honkai-star-rail.fandom.com/wiki/Blade"],
    "Bronya": ["5★ Wind Path: The Harmony", "Supreme Guardian of Belobog", "Leader of the Silvermane Guards | Wiki: https://honkai-star-rail.fandom.com/wiki/Bronya"],
    "Clara": ["5★ Physical Path: The Destruction", "Young girl with a robot guardian", "Accompanied by her mechanical companion Svarog | Wiki: https://honkai-star-rail.fandom.com/wiki/Clara"],
    "Dan Heng": ["4★ Wind Path: The Hunt", "Mysterious youth from the Sky-Faring Commission", "Expert at the art of the spear | Wiki: https://honkai-star-rail.fandom.com/wiki/Dan_Heng"],
    "Dan Heng IL": ["5★ Imaginary Path: The Destruction", "Future Market Supervisor", "Reincarnation of the Dragon of Abundance | Wiki: https://honkai-star-rail.fandom.com/wiki/Dan_Heng_•_Imbibitor_Lunae"],
    "Dr Ratio": ["5★ Imaginary Path: The Hunt", "Renowned physician from Penacony", "Expert in both medicine and combat | Wiki: https://honkai-star-rail.fandom.com/wiki/Dr._Ratio"],
    "Fu Xuan": ["5★ Quantum Path: The Preservation", "Helm Master of the Xianzhou Luofu", "Master of defensive arts | Wiki: https://honkai-star-rail.fandom.com/wiki/Fu_Xuan"],
    "Gallagher": ["4★ Fire Path: The Abundance", "President of the Space Salvation Commission", "Leader of the Intelligentsia Guild | Wiki: https://honkai-star-rail.fandom.com/wiki/Gallagher"],
    "Gepard": ["5★ Ice Path: The Preservation", "Captain of the Silvermane Guards", "Noble defender of Belobog | Wiki: https://honkai-star-rail.fandom.com/wiki/Gepard"],
    "Guinaifen": ["4★ Fire Path: The Nihility", "Popular Podcast Host", "Enthusiastic reporter from the Xianzhou Luofu | Wiki: https://honkai-star-rail.fandom.com/wiki/Guinaifen"],
    "Himeko": ["5★ Fire Path: The Destruction", "Captain of the Astral Express", "Scientist from the Herta Space Station | Wiki: https://honkai-star-rail.fandom.com/wiki/Himeko"],
    "Hook": ["4★ Fire Path: The Destruction", "Member of the Mining Commission", "Explosive expert from the Underworld | Wiki: https://honkai-star-rail.fandom.com/wiki/Hook"],
    "Huohuo": ["5★ Wind Path: The Abundance", "Fortune Teller", "Mysterious prophet from the Xianzhou | Wiki: https://honkai-star-rail.fandom.com/wiki/Huohuo"],
    "Jing Yuan": ["5★ Lightning Path: The Erudition", "Cloud Knight General", "Leader of the Cloud Knights | Wiki: https://honkai-star-rail.fandom.com/wiki/Jing_Yuan"],
    "Kafka": ["5★ Lightning Path: The Nihility", "Enigmatic member of the Stellaron Hunters", "Master of intelligence gathering | Wiki: https://honkai-star-rail.fandom.com/wiki/Kafka"],
    "Luka": ["4★ Physical Path: The Nihility", "Rising Star from Penacony", "Talented performer with mysterious powers | Wiki: https://honkai-star-rail.fandom.com/wiki/Luka"],
    "Lynx": ["4★ Quantum Path: The Abundance", "Mechanical Engineer", "Expert in robotics and repair | Wiki: https://honkai-star-rail.fandom.com/wiki/Lynx"],
    "March 7th": ["4★ Ice Path: The Preservation", "Cheerful girl with mysterious origins", "Found frozen in eternal ice | Wiki: https://honkai-star-rail.fandom.com/wiki/March_7th"],
    "Misha": ["4★ Ice Path: The Destruction", "Genius Supercomputer Engineer", "Young prodigy from Belobog | Wiki: https://honkai-star-rail.fandom.com/wiki/Misha"],
    "Natasha": ["4★ Physical Path: The Abundance", "Underground Doctor", "Caring physician of Belobog | Wiki: https://honkai-star-rail.fandom.com/wiki/Natasha"],
    "Pela": ["4★ Ice Path: The Nihility", "Intelligence Officer", "Silvermane Guards special investigator | Wiki: https://honkai-star-rail.fandom.com/wiki/Pela"],
    "Qingque": ["4★ Quantum Path: The Erudition", "Fortune Teller's Apprentice", "Skilled in divination and combat | Wiki: https://honkai-star-rail.fandom.com/wiki/Qingque"],
    "Robin": ["4★ Fire Path: The Hunt", "Lead Singer of Dreamweaver", "Rising star from the Dream's Edge | Wiki: https://honkai-star-rail.fandom.com/wiki/Robin"],
    "Ruan Mei": ["5★ Ice Path: The Harmony", "Genius Researcher", "One of the Four Scholars of the Network | Wiki: https://honkai-star-rail.fandom.com/wiki/Ruan_Mei"],
    "Sampo": ["4★ Wind Path: The Nihility", "Treasure Hunter", "Mysterious adventurer with questionable morals | Wiki: https://honkai-star-rail.fandom.com/wiki/Sampo"],
    "Seele": ["5★ Quantum Path: The Hunt", "Mechanical expert from Belobog", "Swift and deadly combatant | Wiki: https://honkai-star-rail.fandom.com/wiki/Seele"],
    "Serval": ["4★ Lightning Path: The Erudition", "Rock Star of Belobog", "Energetic performer and fighter | Wiki: https://honkai-star-rail.fandom.com/wiki/Serval"],
    "Silver Wolf": ["5★ Quantum Path: The Nihility", "Elite Hacker", "Member of the Stellaron Hunters | Wiki: https://honkai-star-rail.fandom.com/wiki/Silver_Wolf"],
    "Sparkle": ["5★ Quantum Path: The Harmony", "Managing Director of the IPC", "Expert in business and technology | Wiki: https://honkai-star-rail.fandom.com/wiki/Sparkle"],
    "Sushang": ["4★ Physical Path: The Hunt", "Cloud Knights Lieutenant", "Dedicated martial artist | Wiki: https://honkai-star-rail.fandom.com/wiki/Sushang"],
    "Tingyun": ["4★ Lightning Path: The Harmony", "Sky-Faring Commission Manager", "Business expert and diplomat | Wiki: https://honkai-star-rail.fandom.com/wiki/Tingyun"],
    "Topaz": ["5★ Fire Path: The Hunt", "President of Interastral Peace Corporation", "Business mogul and hunter | Wiki: https://honkai-star-rail.fandom.com/wiki/Topaz_and_Numby"],
    "Trailblazer": ["5★ Physical/Fire Path: The Destruction", "The Nameless", "Mysterious traveler with unknown origins | Wiki: https://honkai-star-rail.fandom.com/wiki/Trailblazer"],
    "Welt": ["5★ Imaginary Path: The Nihility", "Former Anti-Entropy Sovereign", "Guardian of Human Rights | Wiki: https://honkai-star-rail.fandom.com/wiki/Welt"],
    "Xueyi": ["4★ Quantum Path: The Destruction", "Minister of Clouds and Rain", "Mysterious figure from the Xianzhou | Wiki: https://honkai-star-rail.fandom.com/wiki/Xueyi"],
    "Yanqing": ["5★ Ice Path: The Hunt", "General of the Cloud Knights", "Young prodigy swordsman | Wiki: https://honkai-star-rail.fandom.com/wiki/Yanqing"],
    "Yukong": ["4★ Imaginary Path: The Harmony", "Sky-Faring Commission Admiral", "Experienced leader and strategist | Wiki: https://honkai-star-rail.fandom.com/wiki/Yukong"],
    "The Herta": ["5 star, Ice, Path: The Erudition | Wiki: https://honkai-star-rail.fandom.com/wiki/The_Herta"],
    "Sunday": ["5★ Imaginary Path: The Harmony", "Robin's Brother| Wiki: https://honkai-star-rail.fandom.com/wiki/Sunday"],
    "Aglaea": ["5 Star Imaginary Path: The Remembrance | Wiki: https://honkai-star-rail.fandom.com/wiki/Aglaea"],
    "Tribbie": ["5★ Quantum Path: The Harmony,  Wiki: https://honkai-star-rail.fandom.com/wiki/Tribbie"],
    "Mydei" : ["5★ Fire Path: The Destruction,  Wiki: https://honkai-star-rail.fandom.com/wiki/Mydei"],
    "Castorice" : ["5★ Quantum Path: The Remembrance,  Wiki: https://honkai-star-rail.fandom.com/wiki/Castorice"],
    "Anaxa" : ["5★ Wind Path: The Erudition,  Wiki: https://honkai-star-rail.fandom.com/wiki/Anaxa"],
}

def perform_search(query):
    if not query:
        return []

    query = query.lower()
    results = []

    for character, details in search_data.items():
        # Check if query matches character name
        if query in character.lower():
            results.extend([f"{character}: {detail}" for detail in details])
            continue

        # Check if query matches any details
        for detail in details:
            if query in detail.lower():
                results.append(f"{character}: {detail}")

    return results


@app.route('/search')
def search():
    from flask import request
    query = request.args.get('q', '')
    results = perform_search(query)
    return jsonify(results)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Star Rail Archives</title>
        <link href="https://fonts.cdnfonts.com/css/ff-din" rel="stylesheet">
        <style>
            body {
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #1a1a1a;
            }
            .search-container {
                text-align: center;
            }
            h1 {
                font-family: 'FF DIN Pro Bold', sans-serif;
                color: #ffffff;
                font-size: 48px;
                margin-bottom: 30px;
            }
            .search-box {
                width: 500px;
                padding: 15px;
                font-size: 18px;
                border: 2px solid #4a90e2;
                border-radius: 25px;
                outline: none;
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
            }
            .search-box::placeholder {
                color: #888;
            }
            .search-results {
                margin-top: 20px;
                color: white;
                text-align: left;
                max-width: 500px;
            }
            .search-results div {
                padding: 10px;
                border-bottom: 1px solid #333;
                margin: 5px 0;
            }
            a {
                color: #ffffff;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="search-container">
            <h1>Star Rail Archives</h1>
            <input type="text" class="search-box" placeholder="Search the archives..." id="searchInput">
            <div id="searchResults" class="search-results"></div>
        </div>
        <script>
            document.getElementById('searchInput').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    const query = this.value;
                    fetch(`/search?q=${encodeURIComponent(query)}`)
                        .then(response => response.json())
                        .then(results => {
                            const resultsDiv = document.getElementById('searchResults');
                            resultsDiv.innerHTML = results.map(result => {
                const wikiUrl = result.match(/Wiki: (https:\/\/[^\s|]+)/);
                if (wikiUrl) {
                    const [fullResult, url] = wikiUrl;
                    const displayText = result.replace(` | ${fullResult}`, '');
                    return `<div><a href="${url}" target="_blank" style="color: #ffffff; text-decoration: none;">${displayText}</a></div>`;
                }
                return `<div>${result}</div>`;
            }).join('');
                        });
                }
            });
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
