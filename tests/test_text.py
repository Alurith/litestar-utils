from litestar_utils import slugify, SlugifyOptions


def test_slugify():
    expected = "this-is-easy"
    input_string = "this is easy"
    assert slugify(input_string) == expected


def test_slugify_trail_hyphens():
    expected = "this-is-easy"
    input_string = "this is easy---"
    assert slugify(input_string) == expected


def test_slugify_long_string():
    expected = "lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit-sed-placerat-nulla-quis-sapien-efficitur-tincidunt-praesent-id-ultrices-ex-aenean-in-pellentesque-orci-id-imperdiet-turpis-morbi-pulvinar-diam-sed-viverra-ullamcorper"  # noqa: E501
    input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed placerat nulla quis sapien efficitur tincidunt. Praesent id ultrices ex. Aenean in pellentesque orci, id imperdiet turpis. Morbi pulvinar diam sed viverra ullamcorper."  # noqa: E501
    assert slugify(input_string) == expected


def test_slugify_whitespace_collapse():
    expected = "should-collapse-whitespaces"
    input_string = " should  collapse  whitespaces  "

    assert slugify(input_string) == expected


def test_slugify_whitespace_non_collapse():
    expected = "should--not---collapse----whitespaces"
    input_string = " should  not   collapse    whitespaces  "
    options = SlugifyOptions(collapse_whitespace=False)
    assert slugify(input_string, options=options) == expected


def test_slugify_special_chars():
    expected = "a-special-char-test"
    input_string = "a #$special    ** char   \t  \n  test"

    assert slugify(input_string) == expected


def test_slugify_special_chars_whitespace_non_collapse():
    expected = "some---special-------chars---------test"
    input_string = "some #$special    ** chars   \t  \n  test"
    options = SlugifyOptions(collapse_whitespace=False)
    assert slugify(input_string, options=options) == expected


def test_slugify_underscore():
    expected = "test-with-_some_-underscores"
    input_string = "_test with _some_ underscores_"

    assert slugify(input_string) == expected
    options = SlugifyOptions(collapse_whitespace=False)
    assert slugify(input_string, options=options) == expected


def test_slugify_custom_separator():
    expected = "this.is.easy"
    input_string = "this is easy"
    options = SlugifyOptions(separator=".")
    assert slugify(input_string, options=options) == expected


def test_slugify_replacement():
    expected = "emailatexmaple-com"
    input_string = "email@exmaple.com"
    options = SlugifyOptions(replacements=[["@", "at"]])
    assert slugify(input_string, options=options) == expected


def test_slugify_multiple_replacement():
    expected = "emailatexmapledotcom"
    input_string = "email@exmaple.com"
    options = SlugifyOptions(replacements=[["@", "at"], [".", "dot"]])
    assert slugify(input_string, options=options) == expected
