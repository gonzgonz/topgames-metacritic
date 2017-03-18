# TopPS4Games-Metacritic 

### Deploy a RESTful API that exposes two GET methods for retrieving the "TOP PS4 Games by Metascore" from metacritic.com


1. The first method, mapped to **/games**, will retrieve the full list of **Top PS4 Games** in an array of JSON elements.

1. The second method, mapped to **/games/<game_title>**, will retrieve only the selected json object if found within the list.

1. If the game title entered in the URL is not found within the list, the API will return a **404 NOT FOUND** error.


## What's inside this repo?  

1. The actual Application source code can be found within the **App/** directory. **"listener.py"** it's the main file, whereas **"topgames.py"** is a module. You will find detailed comments on both.

1. On the top-level dir, you will find a **Vagrantfile** and the **Ansible provisioner scripts** (more on this later) that will set up a development environment to test the app without the pain of installing modules or configuring an environment manually.

1. **"Images"** contain screenshots from browser-based test demonstrations


## Ok, so.... How do I test this?

### Deploy the environment:

1. Clone this repository.

1. Run ```"vagrant up"``` from your command line (vagrant and virtualbox must be installed)

1. Watch the magic happen and the Ansible provisioner kick in! Ignore if the ansible task "[make sure process is not running]" fails on the first run. I'm just force killing a non-existing process (wat?).

1. After ansible finishes deploying, access the application at http://localhost:8080/games and http://localhost:8080/games/<game_title> either from your browser or a tool as curl.


## Unit Tests

1. Call the First method with curl:

```bash
$ curl -v http://localhost:8080/games
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /games HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.43.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 5052
< Server: Werkzeug/0.12.1 Python/2.7.6
< Date: Sat, 18 Mar 2017 20:42:31 GMT
<
[
  {
    "score": 89,
    "title": "Horizon: Zero Dawn"
  },
  {
    "score": 88,
    "title": "NieR: Automata"
  },
  {
    "score": 87,
    "title": "Nioh"
  },
  {
    "score": 86,
    "title": "Night in the Woods"
  },
  {
    "score": 86,
    "title": "Resident Evil 7: biohazard"
  },
  {
    "score": 84,
    "title": "Yakuza 0"
  },
  {
    "score": 84,
    "title": "Momodora: Reverie Under the Moonlight"
  },
  {
    "score": 84,
    "title": "Hatsune Miku: Project Diva Future Tone - Colorful Tone"
  },
  {
    "score": 84,
    "title": "Hatsune Miku: Project Diva Future Tone - Future Sound"
  },
  {
    "score": 83,
    "title": "Danganronpa 1-2 Reload"
  },
  {
    "score": 82,
    "title": "The Walking Dead: The Telltale Series - A New Frontier Episode 1: Ties That Bind Part One"
  },
  {
    "score": 82,
    "title": "The Walking Dead: The Telltale Series - A New Frontier Episode 2: Ties That Bind Part Two"
  },
  {
    "score": 81,
    "title": "Shantae: Half-Genie Hero"
  },
  {
    "score": 80,
    "title": "Forma.8"
  },
  {
    "score": 80,
    "title": "Flywrench"
  },
  {
    "score": 80,
    "title": "Gravity Rush 2"
  },
  {
    "score": 80,
    "title": "Deus Ex: Mankind Divided - A Criminal Past"
  },
  {
    "score": 79,
    "title": "Tales of Berseria"
  },
  {
    "score": 78,
    "title": "For Honor"
  },
  {
    "score": 77,
    "title": "Torment: Tides of Numenera"
  },
  {
    "score": 77,
    "title": "Kingdom Hearts HD 2.8 Final Chapter Prologue"
  },
  {
    "score": 77,
    "title": "Linelight"
  },
  {
    "score": 77,
    "title": "Sniper Elite 4"
  },
  {
    "score": 77,
    "title": "Darknet"
  },
  {
    "score": 77,
    "title": "Chime Sharp"
  },
  {
    "score": 76,
    "title": "Ys Origin"
  },
  {
    "score": 76,
    "title": "The Flame in the Flood: Complete Edition"
  },
  {
    "score": 76,
    "title": "Pinball FX 2: Star Wars Pinball - Rogue One"
  },
  {
    "score": 76,
    "title": "Call of Duty: Infinite Warfare - Sabotage"
  },
  {
    "score": 75,
    "title": "2064: Read Only Memories"
  },
  {
    "score": 75,
    "title": "Resident Evil 7: biohazard - Banned Footage Vol. 1"
  },
  {
    "score": 75,
    "title": "Atelier Firis: The Alchemist and the Mysterious Journey"
  },
  {
    "score": 74,
    "title": "Touhou Genso Wanderer"
  },
  {
    "score": 74,
    "title": "The Turing Test"
  },
  {
    "score": 74,
    "title": "Tom Clancy's Ghost Recon: Wildlands"
  },
  {
    "score": 74,
    "title": "Wild Guns Reloaded"
  },
  {
    "score": 73,
    "title": "Sublevel Zero Redux"
  },
  {
    "score": 73,
    "title": "Styx: Shards of Darkness"
  },
  {
    "score": 73,
    "title": "Typoman: Revised"
  },
  {
    "score": 73,
    "title": "Kona"
  },
  {
    "score": 72,
    "title": "Semispheres"
  },
  {
    "score": 72,
    "title": "Psychonauts in The Rhombus of Ruin"
  },
  {
    "score": 72,
    "title": "Kitty Powers' Matchmaker"
  },
  {
    "score": 71,
    "title": "LEGO Worlds"
  },
  {
    "score": 71,
    "title": "Disc Jam"
  },
  {
    "score": 71,
    "title": "iO"
  },
  {
    "score": 70,
    "title": "Naruto Shippuden: Ultimate Ninja Storm 4 - Road to Boruto"
  },
  {
    "score": 69,
    "title": "Ride 2"
  },
  {
    "score": 69,
    "title": "Dynasty Warriors: Godseekers"
  },
  {
    "score": 68,
    "title": "Malicious Fallen"
  },
  {
    "score": 68,
    "title": "The Incredible Adventures of Van Helsing: Extended Edition"
  },
  {
    "score": 68,
    "title": "DEXED"
  },
  {
    "score": 68,
    "title": "How to Survive 2"
  },
  {
    "score": 67,
    "title": "Loot Rascals"
  },
  {
    "score": 67,
    "title": "Fate/Extella: The Umbral Star"
  },
  {
    "score": 67,
    "title": "Digimon World: Next Order"
  },
  {
    "score": 67,
    "title": "Berserk and the Band of the Hawk"
  },
  {
    "score": 66,
    "title": "Resident Evil 7: biohazard - Banned Footage Vol. 2"
  },
  {
    "score": 63,
    "title": "Ghost Blade HD"
  },
  {
    "score": 63,
    "title": "Siegecraft Commander"
  },
  {
    "score": 63,
    "title": "FlatOut 4: Total Insanity"
  },
  {
    "score": 61,
    "title": "8DAYS"
  },
  {
    "score": 59,
    "title": "Uncanny Valley"
  },
  {
    "score": 58,
    "title": "Subject 13"
  },
  {
    "score": 58,
    "title": "2Dark"
  },
  {
    "score": 57,
    "title": "Lethal VR"
  },
  {
    "score": 55,
    "title": "Earthlock: Festival of Magic"
  },
  {
    "score": 55,
    "title": "Knee Deep"
  },
  {
    "score": 52,
    "title": "VR Ping Pong"
  },
  {
    "score": 50,
    "title": "Divide"
  },
  {
    "score": 49,
    "title": "Mighty Morphin Power Rangers: Mega Battle"
  },
  {
    "score": 49,
    "title": "Double Dragon IV"
  },
  {
    "score": 49,
    "title": "Moto Racer 4"
  },
  {
    "score": 45,
    "title": "Spheroids"
  },
  {
    "score": 38,
    "title": "Dying: Reborn"
  }
  ```

1. GET the object where "title" is "LEGO Worlds":

```bash
$ curl -v http://localhost:8080/games/LEGO%20Worlds
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /games/LEGO%20Worlds HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.43.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 44
< Server: Werkzeug/0.12.1 Python/2.7.6
< Date: Sat, 18 Mar 2017 20:45:27 GMT
<
{
  "score": 71,
  "title": "LEGO Worlds"
}
```








