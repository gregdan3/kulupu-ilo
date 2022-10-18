#!/usr/bin/env python3
import json
import subprocess
import time

OUTPUT_FILE = "nimi_pi_toki_mute.json"

LANGS = ["es", "ja", "tl"]
LANGS_NAME_EN = ["SPANISH", "JAPANESE", "TAGALOG"]
TO_EXEC = ["/bin/trans", "-b", "-t"]
RATE_LIMIT = 10


def subprocess_translate(input_file):
    to_load = open(input_file, "r").read()
    nimi_mute = json.loads(to_load)
    for lang in LANGS:
        for nimi, nimi_meanings in nimi_mute.items():
            for i, meaning in enumerate(nimi_meanings["meanings"]):
                reply = subprocess.check_output(TO_EXEC + [lang, meaning["def"]])
                if reply:
                    reply = reply.decode().strip()
                    nimi_mute[nimi]["meanings"][i][lang] = reply
                    print("OK! %s->%s: %s -> %s" % (nimi, lang, meaning["def"], reply))
                else:
                    print("NO! %s->%s: %s -> %s" % (nimi, lang, meaning["def"], reply))
                time.sleep(RATE_LIMIT)  # dodge rate limiter

    with open(OUTPUT_FILE, "w") as f:
        f.write(json.dumps(nimi_mute))


def main(argv):
    # subprocess_translate(argv.input)
    ...


if __name__ == "__main__":
    ARGV = None
    main(ARGV)
