"""First-run configuration wizard for Artificial Entity (standard library only)."""
from __future__ import annotations

import json
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent / 'data' / 'entity_config.json'


def ask_text(prompt: str, default: str | None = None) -> str:
    while True:
        suffix = f' [{default}]' if default else ''
        value = input(f'{prompt}{suffix}: ').strip()
        if value:
            return value[:80]
        if default:
            return default
        print('Please enter a name.')


def ask_choice(prompt: str, options: list[str], default: int = 1) -> str:
    print(f'\n{prompt}')
    for i, option in enumerate(options, 1):
        print(f'  {i}. {option}')
    while True:
        answer = input(f'Choose 1-{len(options)} [{default}]: ').strip()
        if not answer:
            return options[default - 1]
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print('Please select one of the listed numbers.')


def run_setup(config_path: Path = CONFIG_PATH) -> dict:
    print('\n=== Artificial Entity: First-Time Setup ===\n')
    entity_name = ask_text('What would you like to name your AI?')
    user_name = ask_text('What should your AI call you?')
    personality = ask_choice('Choose a personality:', ['Friendly', 'Playful', 'Curious', 'Professional', 'Custom'])
    custom_personality = ask_text('Describe the personality') if personality == 'Custom' else ''
    communication = ask_choice('Choose a communication style:', ['Casual', 'Balanced', 'Detailed'], 2)
    memory = ask_choice('Enable persistent memory?', ['Yes', 'No']) == 'Yes'

    config = {
        'setup_complete': True,
        'entity_name': entity_name,
        'user_name': user_name,
        'personality': personality.lower(),
        'custom_personality': custom_personality,
        'communication_style': communication.lower(),
        'memory_enabled': memory,
    }
    config_path.parent.mkdir(parents=True, exist_ok=True)
    # Keep newly created settings private to the current OS user where supported.
    with config_path.open('w', encoding='utf-8') as handle:
        json.dump(config, handle, indent=2, ensure_ascii=False)
    try:
        config_path.chmod(0o600)
    except OSError:
        pass
    print(f'\nSetup complete! {entity_name} is ready to meet you, {user_name}.')
    return config


def load_or_setup(config_path: Path = CONFIG_PATH) -> dict:
    if config_path.exists():
        try:
            config = json.loads(config_path.read_text(encoding='utf-8'))
            if isinstance(config, dict) and config.get('setup_complete') and config.get('entity_name') and config.get('user_name'):
                return config
        except (OSError, json.JSONDecodeError):
            print('Saved configuration could not be read. Starting setup again.')
    return run_setup(config_path)


if __name__ == '__main__':
    config = load_or_setup()
    print(f"\n{config['entity_name']}: Hi {config['user_name']}! Nice to meet you!")
