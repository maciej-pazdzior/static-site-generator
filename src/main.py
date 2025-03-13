from textnode import TextNode, TextType

def main():
    test_object = TextNode("This is some anchor text", TextType.LINK , "https://www.boot.dev")
    print(test_object)
        
if __name__ == "__main__":
    main()