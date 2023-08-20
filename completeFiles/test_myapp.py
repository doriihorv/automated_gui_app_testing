import myapp
import unittest
import os

class TestMyApp(unittest.TestCase):
    def test_app_exists(self):
        app = myapp.Pythagorean()
        print(app)
        self.assertIsNotNone(app)

    def test_gui_exists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        print(gui)
        self.assertIsNotNone(gui)

    def test_widgets_exist(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        self.assertIsNotNone(widgets)

        self.assertEqual(len(widgets),5)
    
    def test_assets_exist(self):
        cwd = os.getcwd()
        img1 = os.path.join(cwd, "assets", "diagram.png")
        img2 = os.path.join(cwd, "assets", "logo.png")
        self.assertEqual(os.path.isfile(img1), True)
        self.assertEqual(os.path.isfile(img2), True)

    def test_dict_exists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        output = gui.pythagorean()
        self.assertIsInstance(output, dict)

        for key, val in output.items():
            self.assertIsInstance(key,str)
            self.assertIsInstance(val,str)

    def test_inputAB(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]
        inputA.text = "3"
        inputB.text = "4"
        output = gui.pythagorean()

        self.assertEqual(output,{"c":"5.0"})

    def test_inputABC(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]
        inputC = (widgets[1].children)[0]

        inputA.text = "3"
        inputB.text = "4"
        inputC.text = "5"

        output = gui.pythagorean()
        self.assertEqual(output, {'error': "if you already know ALL sides then you don't need me!"})
    
    def test_inputABwrong(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]

        inputA.text = "3"
        inputB.text = "-4"

        output = gui.pythagorean()
        print(output)
        self.assertNotEqual(output,{"c":"5.0"}) 




if __name__ == "__main__":
    unittest.main()