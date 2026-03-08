# Name: Ethan Mayer
# Date: March 3, 2026

import json, time, random
from string import ascii_lowercase
import datetime

QUESTIONS = {
    "History": {
        "First Emperor of unified China?":      ["Qin Shi Huang", "Wu of Han",   "Kublai Khan",  "Sun Yat-sen"],
        "Year the Magna Carta was signed?":     ["1215",          "1066",         "1492",         "1348"],
        "Year the French Revolution began?":    ["1789",          "1776",         "1805",         "1812"],
        "Empire ruled by Genghis Khan?":        ["Mongol",        "Ottoman",      "Roman",        "Persian"],
        "Year the Berlin Wall fell?":           ["1989",          "1985",         "1991",         "1993"],
    },
    "Science": {
        "Powerhouse of the cell?":              ["Mitochondria",  "Nucleus",      "Ribosome",     "Golgi"],
        "Speed of light in a vacuum?":          ["300,000 km/s",  "150,000 km/s", "450,000 km/s", "100,000 km/s"],
        "Chemical symbol for Gold?":            ["Au",            "Go",           "Gd",           "Ag"],
        "Human chromosome count?":              ["46",            "23",           "44",           "48"],
        "Planet with the most moons?":          ["Saturn",        "Jupiter",      "Uranus",       "Neptune"],
    },
    "Music": {
        "Band behind 'Dark Side of the Moon'?": ["Pink Floyd",    "Led Zeppelin", "The Beatles",  "The Stones"],
        "Composer of the Moonlight Sonata?":    ["Beethoven",     "Mozart",       "Bach",         "Chopin"],
        "Strings on a standard guitar?":        ["6",             "4",            "5",            "8"],
        "The 'King of Pop'?":                   ["Michael Jackson","Prince",      "Bowie",        "Mercury"],
        "Notes in a musical octave?":           ["8",             "6",            "7",            "12"],
    },
}
SCORE_FILE, TIME_LIMIT, BASE_PTS, MAX_BONUS = "scores.json", 15, 100, 50

def load_scores():
    try:    return json.load(open(SCORE_FILE))
    except: return []

def save_score(record):
    """Append a game result to the scores history file."""
    scores = load_scores()
    scores.append(record)
    json.dump(scores, open(SCORE_FILE, "w"), indent=2)

def choose_category():
    """Ask the user to pick a category; re-prompt on invalid input."""
    labeled = dict(zip(ascii_lowercase, QUESTIONS))
    print("\nCategories: " + "  ".join(f"{k}. {v}" for k, v in labeled.items()))
    while (pick := input("Choose: ").strip().lower()) not in labeled:
        print(f"  Enter one of: {', '.join(labeled)}")
    return labeled[pick]

def ask_question(num, total, question, options):
    """Show one question with labeled options; re-prompt on invalid input.
    Returns (is_correct, elapsed_seconds)."""
    correct = options[0]                             # first item is always correct
    labeled = dict(zip(ascii_lowercase, sorted(options)))
    print(f"\nQuestion {num} of {total}: {question}")
    for label, option in labeled.items():
        print(f"  {label}. {option}")
    start = time.time()
    while (pick := input("Choice? ").strip().lower()) not in labeled:
        print(f"  Enter one of: {', '.join(labeled)}")
    elapsed = time.time() - start
    if labeled[pick] == correct:
        bonus = max(0, round((1 - elapsed / TIME_LIMIT) * MAX_BONUS)) if elapsed <= TIME_LIMIT else 0
        print(f"  Correct! +{BASE_PTS + bonus} pts (speed bonus: +{bonus})  [{elapsed:.1f}s]")
        return True, elapsed
    else:
        print(f"  The answer is '{correct}' not {labeled[pick]!r}  [{elapsed:.1f}s]")
        return False, elapsed

def show_history():
    """Print the top-10 all-time scores from the history file."""
    rows = sorted(load_scores(), key=lambda s: s["score"], reverse=True)[:10]
    if rows:
        print(f"\n{'#':<3}{'Player':<14}{'Category':<10}{'Score':>6}  Date\n{'─'*44}")
        for i, s in enumerate(rows, 1):
            print(f"{i:<3}{s['player']:<14}{s['category']:<10}{s['score']:>6}  {s['date'][:10]}")

def main():
    print("═══ QuizMaster ═══")
    name     = input("Your name: ").strip() or "Player"
    category = choose_category()
    num_correct = total_score = 0
    for num, (question, options) in enumerate(random.sample(list(QUESTIONS[category].items()), 5), start=1):
        correct, elapsed = ask_question(num, 5, question, options)
        if correct:
            bonus        = max(0, round((1 - elapsed / TIME_LIMIT) * MAX_BONUS)) if elapsed <= TIME_LIMIT else 0
            total_score += BASE_PTS + bonus
            num_correct += 1
    print(f"\nYou got {num_correct} out of 5 correct — {total_score} pts.")
    prev_high = max((s["score"] for s in load_scores()), default=0)
    save_score({"player": name, "category": category, "score": total_score,
                "correct": num_correct, "date": datetime.datetime.now().isoformat()})
    if total_score > prev_high:
        print("🏆 NEW HIGH SCORE!")
    show_history()

if __name__ == "__main__":
    main()