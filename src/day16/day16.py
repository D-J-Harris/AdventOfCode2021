import math

if __name__ == "__main__":

    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    with open('inputs/input-16.txt', 'r') as f:
        puzzle_binary = ''.join([hex_to_bin[c] for c in f.readline()])

    class Packet:
        def __init__(self, version, packet_type, parent):
            self.version = version
            self.packet_type = packet_type
            self.is_literal = self.packet_type == 4
            self.parent = parent
            self.children = []
            self.value = None
            self.size = None

        def __str__(self) -> str:
            return ('\n' +
                f'version: {self.version}\n' +
                f'is literal: {self.is_literal}\n' +
                f'children: {self.children}\n' +
                f'size: {self.size}\n' +
                f'value: {self.value}')


    def parse(binary, parent):
        ptr = 0
        version = int(binary[ptr: (ptr := ptr + 3)], 2)
        packet_type = int(binary[ptr: (ptr := ptr + 3)], 2)
        packet = Packet(version, packet_type, parent)

        if packet.is_literal:
            num = ''
            while int(binary[ptr: (ptr := ptr + 1)], 2):
                num += binary[ptr: (ptr := ptr + 4)]
            num += binary[ptr: (ptr := ptr + 4)]
            packet.value = int(num, 2)
            packet.size = ptr
            return packet, binary[ptr:]
        else:
            length_type = int(binary[ptr: (ptr := ptr + 1)], 2)
            length_num_subpackets = int(binary[ptr: (ptr := ptr + (11 if length_type else 15))], 2)
            child_binary = binary[ptr:]
            while length_num_subpackets > 0:
                child_packet, child_binary = parse(child_binary, packet)
                packet.children.append(child_packet)
                length_num_subpackets -= 1 if length_type else child_packet.size
            ptr += sum([x.size for x in packet.children])
            packet.size = ptr
            match packet.packet_type:
                case 0:
                    packet.value = sum([x.value for x in packet.children])
                case 1:
                    packet.value = math.prod([x.value for x in packet.children])
                case 2:
                    packet.value = min([x.value for x in packet.children])
                case 3:
                    packet.value = max([x.value for x in packet.children])
                case 5:
                    packet.value = packet.children[0].value > packet.children[1].value
                case 6:
                    packet.value = packet.children[0].value < packet.children[1].value
                case 7:
                    packet.value = packet.children[0].value == packet.children[1].value
            return packet, binary[ptr:]


    def version_sum(root_packet):
        ans = root_packet.version
        for child in root_packet.children:
            ans += version_sum(child)
        return ans

    outer_packet, _ = parse(puzzle_binary, None)
    print(f'answer to puzzle 1 is {version_sum(outer_packet)}')
    print(f'answer to puzzle 2 is {outer_packet.value}')
