def check_colors_and_textures(string):
    """
    Function for checking if any colors or textures are present in the given string.

    Args:
        string (str): A string to check for the presence of colors or textures.

    Returns:
        A tuple containing two lists of strings:
        - The first list contains the colors present in the string.
        - The second list contains the textures present in the string.
    """

    colors = ["Red",    "Orange",    "Yellow",    "Green",    "Blue",    "Purple",
                  "Pink",    "Brown",    "Gray",    "Black",    "White",    "Beige",
                          "Turquoise",    "Teal",    "Magenta",    "Lavender",
                                  "Indigo",    "Maroon",    "Gold",    "Silver", 
                                        "Bronze",    "Copper",    "Olive",    "Navy",
                                            "Sky blue",
          "Cream",    "Peach",    "Rose",    "Fuchsia",    "Coral",    "Mint",
            "Chartreuse",    "Salmon",    "Sienna",    "Slate",    "Tan",
              "Crimson",    "Ivory",    "Khaki",    "Lilac",    "Mauve",
                "Mustard",    "Rust",    "Scarlet",    "Tangerine",
                "Vermilion",    "Violet",    "Wheat",    "Brick red",    "Caramel"]


    textures = ["Smooth",    "Rough",    "Fuzzy",    "Soft", "Hard",
                  "Bumpy",    "Slick",    "Sticky",    "Grainy",
                      "Sandy",    "Slippery",    "Jagged",    "Sharp",
                        "Coarse",    "Silky",    "Velvety",    "Wet",
                        "Dry",    "Glossy",    "Matte",    "Sparkly",
                        "Metallic",    "Wooden",    "Leathery",
                        "Plastic",    "Rubber",    "Furry", "Woolly",    "Feathery",
                        "Smooth",    "Satin",    "Lace",    "Crochet",    "Knitted",
                        "Embroidered",    "Linen",    "Silk",    "Velvet",    "Suede",
                        "Corduroy",    "Denim",    "Felt",    "Tweed",    "Mesh",
            "Hairy",    "Crisp",    "Crumbly",    "Flaky",    "Puffy",    "Spongy", 
                "Crunchy",    "Chewy",    "Gummy",    "Slimy",    "Starchy",    "Syrupy",
                        "Icy",    "Rocky",    "Stony",    "Sandy",    "Peppery",    "Salty",
                            "Sour",    "Sweet",    "Tangy",    "Tart",    "Spicy", 
                                      "Herbaceous",    "Earthy",    "Mossy",    "Woody", 
                                "Smoky",    "Smokey",    "Rusty",    "Corroded",    "Weathered",
                            "Rugged",    "Smooth",    "Polished",    "Shiny",    "Gleaming",
                        "Dull",    "Muddy",    "Cloudy",    "Milky",    "Transparent",
                                "Translucent",    "Opaque"]

    # Initialize empty lists for colors and textures present in the string
    colors_present = []
    textures_present = []
    # Check if any of the colors are present in the string
    for color in colors:
        if color.lower() in string.lower():
            if (color.lower() != "white") | ((color.lower() == "white") & ("background" not in string.lower())):
                colors_present.append(color)
    # Check if any of the textures are present in the string
    for texture in textures:
        if texture.lower() in string.lower():
            textures_present.append(texture)
    # Return boolean values indicating whether any colors or textures are present,
    # as well as the list of colors and textures present in the string
    return colors_present, textures_present
