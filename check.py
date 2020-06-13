import unittest

def check(selection, userSel):
  white = 0
  diff = [selection[i] == userSel[i] for i in range(len(selection))]
  black = sum(diff)
  iter = [i for i in range(len(selection)) if not diff[i]]
  for i in iter:
    for j in range(len(selection)):
      if (not diff[j]) and userSel[i] == selection[j]:
          white = white + 1
          diff[j] = True

  return black, white

class TestCheck(unittest.TestCase):

  def test_check_all_black(self):
    self.assertEqual(check([0,1,2,3,4], [0,1,2,3,4]), (5,0))
  def test_check_one_black(self):
    self.assertEqual(check([0,1,2,3,4], [4,4,4,4,4]), (1,0))
  def test_check_one_not(self):    
    self.assertEqual(check([0,1,2,4,4], [0,1,2,3,4]), (4,0))
  def test_check_one_one_black_four_whites(self):        
    self.assertEqual(check([0,1,2,3,4], [4,3,2,1,0]), (1,4))
  def test_check_all_whites(self):        
    self.assertEqual(check([0,1,2,3,4], [4,2,3,1,0]), (0,5))

if __name__ == '__main__':
    unittest.main()