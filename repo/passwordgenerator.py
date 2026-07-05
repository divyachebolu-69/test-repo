import random
import string
import argparse


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                      use_digits=True, use_symbols=True, exclude_ambiguous=False):
    """
    Generate a secure random password.

    Args:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters (A-Z)
        use_lowercase (bool): Include lowercase letters (a-z)
        use_digits (bool): Include digits (0-9)
        use_symbols (bool): Include symbols (!@#$%^&*...)
        exclude_ambiguous (bool): Exclude ambiguous chars like 0, O, l, 1, I

    Returns:
        str: Generated password
    """
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Remove ambiguous characters if requested
    if exclude_ambiguous:
        ambiguous = "0O1lI|`"
        characters = "".join(c for c in characters if c not in ambiguous)

    # Ensure at least one character from each selected category
    password = []
    if use_uppercase:
        chars = string.ascii_uppercase
        if exclude_ambiguous:
            chars = "".join(c for c in chars if c not in "OI")
        password.append(random.choice(chars))
    if use_lowercase:
        chars = string.ascii_lowercase
        if exclude_ambiguous:
            chars = "".join(c for c in chars if c not in "l")
        password.append(random.choice(chars))
    if use_digits:
        chars = string.digits
        if exclude_ambiguous:
            chars = "".join(c for c in chars if c not in "01")
        password.append(random.choice(chars))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest randomly
    remaining = length - len(password)
    password += random.choices(characters, k=remaining)

    # Shuffle to avoid predictable positions
    random.shuffle(password)

    return "".join(password)


def check_strength(password):
    """
    Check the strength of a password.

    Returns:
        tuple: (strength_label, score, tips)
    """
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add uppercase letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add digits")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add special symbols")

    if score <= 3:
        label = "Weak"
    elif score <= 5:
        label = "Moderate"
    elif score == 6:
        label = "Strong"
    else:
        label = "Very Strong"

    return label, score, tips


def generate_multiple(count=5, **kwargs):
    """Generate multiple passwords at once."""
    return [generate_password(**kwargs) for _ in range(count)]


def main():
    parser = argparse.ArgumentParser(description="🔐 Python Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Password length (default: 12)")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="Number of passwords to generate (default: 1)")
    parser.add_argument("--no-upper", action="store_true",
                        help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true",
                        help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true",
                        help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true",
                        help="Exclude symbols")
    parser.add_argument("--no-ambiguous", action="store_true",
                        help="Exclude ambiguous characters (0, O, 1, l, I)")
    parser.add_argument("--check", type=str,
                        help="Check strength of a given password")

    args = parser.parse_args()

    # Check strength mode
    if args.check:
        label, score, tips = check_strength(args.check)
        print(f"\nPassword : {args.check}")
        print(f"Strength : {label} (score: {score}/7)")
        if tips:
            print("Tips     :")
            for tip in tips:
                print(f"  - {tip}")
        return

    # Generate passwords
    options = {
        "length": args.length,
        "use_uppercase": not args.no_upper,
        "use_lowercase": not args.no_lower,
        "use_digits": not args.no_digits,
        "use_symbols": not args.no_symbols,
        "exclude_ambiguous": args.no_ambiguous,
    }

    print(f"\n🔐 Generated Password{'s' if args.count > 1 else ''}:\n")
    for i, pwd in enumerate(generate_multiple(args.count, **options), 1):
        label, score, _ = check_strength(pwd)
        print(f"  {i}. {pwd}  [{label}]")

    print()


if __name__ == "__main__":
    main()