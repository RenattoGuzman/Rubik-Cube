class RubiksCube:
    def __init__(self):
        self.cube = {
            'U': [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']],
            'F': [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']],
            'R': [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']],
            'L': [['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']],
            'B': [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']],
            'D': [['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']]
        }

    def display(self):
        for face, values in self.cube.items():
            print(face)
            for row in values:
                print(row)
            print()

            
    def rotate_face_clockwise(self, face):
        # Rotate the stickers on the specified face clockwise
        self.cube[face] = list(zip(*reversed(self.cube[face])))
        # Update neighboring faces
        if face == 'U':
            self._rotate_neighboring_clockwise_U()
        elif face == 'D':
            self._rotate_neighboring_clockwise_D()
        elif face == 'L':
            self._rotate_neighboring_clockwise_L()
        
        elif face == 'R':
            self._rotate_neighboring_clockwise_R()
        elif face == 'F':
            self._rotate_neighboring_clockwise_F()
        elif face == 'B':
            self._rotate_neighboring_clockwise_B()

    def rotate_face_counterclockwise(self, face):
        # Rotate the stickers on the specified face counterclockwise
        self.cube[face] = list(reversed(list(zip(*self.cube[face]))))
        # Update neighboring faces
        if face == 'U':
            self._rotate_neighboring_counterclockwise('F', 'L', 'B', 'R')
        elif face == 'D':
            self._rotate_neighboring_counterclockwise('B', 'R', 'F', 'L')
        elif face == 'L':
            self._rotate_neighboring_counterclockwise('U', 'F', 'D', 'B')
        elif face == 'R':
            self._rotate_neighboring_counterclockwise('U', 'B', 'D', 'F')
        elif face == 'F':
            self._rotate_neighboring_counterclockwise('U', 'L', 'D', 'R')
        elif face == 'B':
            self._rotate_neighboring_counterclockwise('U', 'R', 'D', 'L')

    def _rotate_neighboring_clockwise_U(self):
        # Helper method to rotate neighboring faces clockwise
        face1 = 'F'
        face2 = 'R'
        face3 = 'B'
        face4 = 'L'
        
        temp_face = list(self.cube[face1][0]) 

        self.cube[face1][0] = self.cube[face2][0]
        self.cube[face2][0] = self.cube[face3][0]
        self.cube[face3][0] = self.cube[face4][0]
        self.cube[face4][0] = temp_face
        
    def _rotate_neighboring_clockwise_D(self):
        # Helper method to rotate neighboring faces clockwise
        face1 = 'B'
        face2 = 'R'
        face3 = 'F'
        face4 = 'L'
        temp_face = list(self.cube[face1][2]) 
        print(temp_face)
        self.cube[face1][2] = self.cube[face2][2]
        self.cube[face2][2] = self.cube[face3][2]
        self.cube[face3][2] = self.cube[face4][2]
        self.cube[face4][2] = temp_face

    def _rotate_neighboring_clockwise_L(self):
        # Helper method to rotate neighboring faces clockwise
        face1 = 'U'
        face2 = 'B'
        face3 = 'D'
        face4 = 'F'
        
        # Save the columns of face1
        face_1 = [self.cube[face1][i][0] for i in range(3)]
        face_2 = [self.cube[face2][2-i][2] for i in range(3)]
        face_3 = [self.cube[face3][2-i][0] for i in range(3)]
        face_4 = self.cube[face4]


        # Update face1 with columns from face2, face2 with columns from face3, and so on
        for i in range(3):

            self.cube[face1][i][0] = face_2[i] # U
            self.cube[face2][i][2] = face_3[i] # B
            self.cube[face3][i][0] = self.cube[face4][i][0] #D
            self.cube[face4][i][0] = face_1[i] # F

        
    def _rotate_neighboring_counterclockwise(self, face1, face2, face3, face4):
        # Helper method to rotate neighboring faces counterclockwise
        temp_face = list(self.cube[face1][2])
        self.cube[face1][2] = self.cube[face4][0]
        self.cube[face4][0] = self.cube[face3][0]
        self.cube[face3][0] = self.cube[face2][2]
        self.cube[face2][2] = temp_face

# Create an instance of RubiksCube
cube = RubiksCube()

cube.rotate_face_clockwise('L')
cube.rotate_face_clockwise('U')

cube.display()

