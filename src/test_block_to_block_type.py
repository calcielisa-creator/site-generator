import unittest

from blocktype import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_block_type_paragraph(self):
        block = "This is a normal paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_type_heading_one(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_block_type_heading_four(self):
        block = "#### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)
    
    def test_block_type_heading_six(self):
        block = "###### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_block_type_heading_seven(self):
        block = "####### This is not a heading"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.HEADING, block_type)

    def test_block_type_heading_no_space(self):
        block = "###fThis is not a heading"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.HEADING, block_type)
    
    def test_block_type_quote_block(self):
        block = "> This is a quote\n>block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)       
            
    def test_block_type_quote_block_one_line(self):
        block= "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type) 
      
    def test_block_type_quote_block_wrong(self):
        block = "> This is not\n- a quote block"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.QUOTE, block_type) 

    def test_block_type_unordered_list(self):
        block = "- This is an unordered list\n- with items"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)       
            
    def test_block_type_unordered_list_one_line(self):
        block= "- This is an unordered list"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type) 
      
    def test_block_type_unordered_list_wrong(self):
        block = "- This is not\n2- an unordered list"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.UNORDERED_LIST, block_type) 


    def test_block_type_ordered_list(self):
        block = "1. This is an ordered list\n2. with items"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)       
            
    def test_block_type_ordered_list_one_line(self):
        block = "1. This is an ordered list"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type) 
      
    def test_block_type_ordered_list_wrong(self):
        block = "1. This is not\n3. an ordered list"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.ORDERED_LIST, block_type) 
    
    def test_block_type_ordered_list_wrong_start(self):
        block = "2. This is not\n3. an ordered list"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.ORDERED_LIST, block_type) 

    def test_block_type_code_blocks(self):
        block = "```\nThis is a code block\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_block_type_code_blocks_no_closure(self):
        block = "```\nThis is not a code block"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.CODE, block_type)

    def test_block_type_code_blocks_wrong_opening(self):
        block = "```This is not\n a code block\n```"
        block_type = block_to_block_type(block)
        self.assertNotEqual(BlockType.CODE, block_type)