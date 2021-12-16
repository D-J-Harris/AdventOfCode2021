
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
                f'value: {self.value}')


    def parse(binary, parent):

        ptr = 0
        version = int(binary[ptr: (ptr := ptr + 3)], 2)
        type = int(binary[ptr: (ptr := ptr + 3)], 2)
        packet = Packet(version, type, parent)

        if packet.is_literal:
            num = ''
            while int(binary[ptr: (ptr := ptr + 1)], 2):
                num += binary[ptr: (ptr := ptr + 4)]
            num += binary[ptr: (ptr := ptr + 4)]
            ptr += (ptr - 6) % 5
            packet.value = int(num, 2)
            packet.size = ptr
            return packet, binary[ptr:]
        else:
            length_type = int(binary[ptr: (ptr := ptr + 1)], 2)
            length_num_subpackets = int(binary[ptr: (ptr := ptr + (11 if length_type else 15))], 2)
            binary = binary[ptr:]
            while length_num_subpackets > 0:
                child_packet, binary = parse(binary, packet)
                length_num_subpackets -= 1 if length_type else child_packet.size
                packet.children.append(child_packet)
            children_size = sum([x.size for x in packet.children])
            packet_size = children_size + (4 - (children_size % 4))
            while binary[packet_size: packet_size + 4] == '0000':
                packet_size += 4
            packet.size = packet_size
            if parent:
                parent.children.append(packet)
            return packet, binary[packet.size:]


    p, _ = parse(puzzle_binary, None)
    print(p)
    [print(x) for x in p.children]
