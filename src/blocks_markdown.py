def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        # Strip the entire block
        block = block.strip()
        # If it's not empty, process inner lines
        if block:
            # Split by newlines, strip each line, and rejoin
            lines = [line.strip() for line in block.split("\n")]
            cleaned_blocks.append("\n".join(lines))
    return cleaned_blocks