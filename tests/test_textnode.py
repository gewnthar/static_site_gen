def test_split_nodes_delimiter():
    # Single valid delimiter
    node = TextNode("This is **bold** text", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert result == [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" text", TextType.TEXT),
    ]

    # Multiple delimiters
    node = TextNode("This is **bold** and **italic** text", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert result == [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("italic", TextType.BOLD),
        TextNode(" text", TextType.TEXT),
    ]

    # Unmatched delimiter
    node = TextNode("This is **bold text", TextType.TEXT)
    try:
        split_nodes_delimiter([node], "**", TextType.BOLD)
    except ValueError as e:
        assert str(e) == "Unmatched delimiter '**' in text: This is **bold text"

    # Nested delimiters (not allowed)
    node = TextNode("This is **bold and *italic*** text", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    assert result == [
        TextNode("This is ", TextType.TEXT),
        TextNode("bold and *italic*", TextType.BOLD),
        TextNode(" text", TextType.TEXT),
    ]

