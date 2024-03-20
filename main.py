
#This function performs run length encoding on a string a returns the conpressed string
def RLE_compress(message):
    characters = list(message)
    past_letter = characters[0]
    counter = 0
    chain_length = 0
    compresssed_message = ""
    for letter in characters:
        counter += 1
        if letter == past_letter:
            chain_length += 1
        else:
            compresssed_message += (past_letter + str(chain_length))
            chain_length = 1
        past_letter = letter
        if counter == len(characters):
            compresssed_message += (letter + str(chain_length))
    return compresssed_message

#TEST CODE
def test_answers():
    assert RLE_compress("AABBBAAAABBBBBAAAAAABBBBBBB") == "A2B3A4B5A6B7"
    assert RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFF") == "A2C4B5A7X1F8"
    assert RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFD") == "A2C4B5A7X1F8D1"
    assert RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDD") == "A2C4B5A7X1F8D2"
    assert RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDDD") == "A2C4B5A7X1F8D3"
    assert RLE_compress("ABCDEF") == "A1B1C1D1E1F1" # as discussed, this one doesn't actually "compress", but it's a good test case
    assert RLE_compress("FFFFFFFFFFFFFFFFFFF") == "F19"
    assert RLE_compress("F") == "F1"
    assert RLE_compress("F????") == "F1?4"
    assert RLE_compress("Mmmmmmmmmm sooooo goooooood!") == "M1m9 1s1o5 1g1o7d1!1"
    assert RLE_compress("Booooooooooooo, hisssssssss") == "B1o13,1 1h1i1s9"

