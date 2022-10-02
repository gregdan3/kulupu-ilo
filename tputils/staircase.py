from typing import List, Optional


def rm_str_prefix(str, prefix):
    return str[len(prefix) :]


def staircase(
    stairs: str,
    steps: List[str],
    past: Optional[List[str]] = None,
    paths: Optional[List[List[str]]] = None,
) -> Optional[List[List[str]]]:
    """Given a 'staircase' string, return all possible paths through that
    string given a list of possible steps. Returns None if not possible.
    The complexity here is **bad**. This is depth first."""
    if past is None:
        past = []
    if paths is None:
        paths = []
    if not steps:
        return
    if not stairs:
        if past:
            paths.append(past)
        return

    for step in steps:
        if stairs.startswith(step):
            staircase(rm_str_prefix(stairs, step), steps, past + [step], paths)
    return paths


def main():
    stairs = "aa"
    steps = ["a"]
    print(staircase(stairs, steps))


if __name__ == "__main__":
    main()
