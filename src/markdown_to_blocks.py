def markdown_to_blocks(markdown):
    line_blocks = markdown.split('\n\n')
    tidy_line_blocks = []
    for block  in line_blocks:
        if block == "":
            continue
        tidy_line_blocks.append(block.strip())

    return tidy_line_blocks