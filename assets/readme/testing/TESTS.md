# **Contents**

- ## [Tests]()
    - 

# **Tests**

## **Read Instructions**

### Valid Inputs
- If the user wishes to read the instructions, the following inputs will be accepted (Y, N, y, n). The screenshots of my testing for valid inputs can be found [here](./images/valid-input/instructions).

### Invalid Inputs
- Anything other than valid input will not be accepted. This is due to the game checking for the exact valid inputs. I have tested all invalid inputs and they can be found [here](./images/invalid-input/instructions).

## **Select Difficulty**

### Valid Inputs
- To select a difficulty, the user must enter the number corresponding to the difficulty. Only the following inputs will be accepted (0, 1, 2, 3, 4, 5). The screenshots of testing these can be found [here](./images/valid-input/difficulty).

The screenshots for these tests have been done within the terminal of my code editor. This is due to the console being cleared after selecting a difficulty. In order to show the tests, I temporarily disabled this feature.

### Invalid Inputs
- To ensure a valid input, the user's input is checked to ensure that it is a number. After this, it is then checked to ensure that it is equal or greater than 0 and less than 6. Screenshots of my testing can be found [here](./images/invalid-input/difficulty).