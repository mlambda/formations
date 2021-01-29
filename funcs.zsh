function dev-python-tikz() {
    local py="$1"
    local tex="${1%.py}.tex"
    echo "$py" | entr -c sh -c 'python '"$py"' > '"$tex"' && latexmk '"$tex"
}