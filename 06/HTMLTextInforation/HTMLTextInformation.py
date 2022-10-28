class HTMLTextInformation:
    special_symbols = r"\/|-+=!@'<>?— .,()&^{}%$#:↑;`~'" + r'"'

    headers = [
        "h1", "h2", "h3", "h4", "h5", "h6",
    ]
    test_formatting = [
        "b", "em", "i", "small", "strong",
        "sub", "sup", "ins", "del", "mark",
    ]

    input_text = [
        "code", "kbd", "samp", "var", "pre"
    ]

    citations_and_definitions = [
        "abbr", "bdo", "blockquote", "q", "cite", "dfn",
    ]

    paragraphs_text_wrappers = [
        "p", "br", "hr",
    ]

    all_text_information = [
        *headers,
        *test_formatting,
        *input_text,
        *citations_and_definitions,
        *paragraphs_text_wrappers,
    ]
