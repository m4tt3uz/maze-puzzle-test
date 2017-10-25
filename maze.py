import os
import sys
import json
from terminaltables import AsciiTable


class Maze(object):

    def __init__(self, start_node, json_file, selected_objects=[]):
        self.start_node = start_node
        self.selected_objects = selected_objects
        self.result = [['Id', 'Room', 'Obj. collected']]
        self.json_file = json_file

    def reprint_result(self):
        print (AsciiTable(self.result).table)

    def start_game(self):
        """ Let'go !"""
        self.my_rooms = self._build_dict_rooms(self._get_rooms(self.json_file))
        self._check_room(self.my_rooms.get(str(self.start_node)))
        return self.result

    def _build_dict_rooms(self, rooms):
        """Change list in key/value dict"""
        dict_rooms = {}
        for room in rooms:
            dict_rooms[str(room['id'])] = room
        return dict_rooms

    def _get_rooms(self, file_name):
        """Get Rooms from Json file"""
        try:
            print ('Reading rooms...')
            file_opened = open(file_name)
            json_file = json.load(file_opened)
            json_root = json_file['rooms']
            print ('N. of rooms is %s ' % len(json_root))
            return json_root
        except Exception as ex:
            print ('Error during reading file!')
            print (ex)
            return None

    def _check_room(self, room):
        """Search selected objects in room"""
        try:
            founded_obj = []

            if room.get('objects') is not None:
                for elem in room.get('objects'):
                    possible_obj= elem.get('name').upper()
                    if possible_obj in (val.upper() for val in self.selected_objects):
                        founded_obj.append(possible_obj)

            if founded_obj:
                self.result.append([room['id'], room['name'], ','.join(founded_obj)])
            else:
                self.result.append([room['id'], room['name'], "None"])
            self._move_to_room(room)
        except Exception as ex:
            print ("Error in _check_rooms")
            print (ex)
            return None

    def _move_to_room(self, room):
        """ Go to next room via direction """
        coordinates = ['north', 'south', 'west', 'east']
        for direction in coordinates:
            if room.get(direction) is not None:
                next_room = self.my_rooms.get(str(room[direction]))
                del room[direction]
                self._check_room(next_room)


def execute_code():
    """ Evaluate parameter """
    try:
        parameters = sys.argv
        json_file = parameters[1]
        if os.path.isfile(json_file) is False:
            print ('Please, check json path!')
            return None

        start_node = parameters[2]
        if int(start_node) != 0:
            print ('FIRST ROOM: %s' % start_node)
        else:
            print ('Please, choose correct start room id [1..N]')
            return None

        selected_obj = []
        for item in parameters[3:]:
            if item:
                print ("SELECTED OBJECT: %s" %  item)
                selected_obj.append(item)

        if len(selected_obj) == 0:
            print ('Please, check json path!')
            return None
        maze = Maze(start_node, json_file, selected_obj)
        result = maze.start_game()
        return result
    except Exception as ex:
        print ("Error during execution!")
        print (ex)
        return None



if __name__ == "__main__":
    result = execute_code()
    if result is None:
        print ("No result!")
    else:
        print (AsciiTable(result).table)

