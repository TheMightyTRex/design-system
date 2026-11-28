#!/usr/bin/env bash
# Runs the privacy check, the On this page check and the banned words check before every commit in this clone.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
cat > .git/hooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
tools/check-private.sh --staged || exit 1
python3 tools/check_on_this_page.py || exit 1
exec python3 tools/check_words.py
HOOK
chmod +x .git/hooks/pre-commit
echo "Pre-commit privacy and banned words checks installed."
