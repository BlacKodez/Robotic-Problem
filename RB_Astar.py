def aStarAlgo(start_node, stop_node):

    open_set = set(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {  }# parents contains an adjacency map of all nodes

    # ditance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node


    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v


        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                # for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n

                        # if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)

            path.reverse()

            print('Path found: {}'.format(path))
            return path


        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


# define fuction to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# for simplicity we ll consider heuristic distances given
# and this function returns heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'S': 0,
        '3': 0,
        '4': 0,
        'G': 0,
        '7': 0,
        '9': 0,
        '10': 0,
        '12': 0,
        '13': 0,
        '14': 0,
        '15': 0,
        '16': 0,
        '18': 0,
        '19': 0,
        '20': 0,
        '22': 0,
        '24': 0,
        '25': 0,
        '26': 0,
        '28': 0,
        '29': 0,
        '30': 0,
        '31': 0,
        '32': 0,
        '34': 0,
        '35': 0,
        '36': 0,
        '37': 0,
        '38': 0,
        '40': 0,
        '41': 0,
        '42': 0,
        '43': 0,
        '44': 0,
        '45': 0,
        '46': 0,
        '47': 0,
        '48': 0,
        '49': 0,
        'OBS': 50,

    }

    return H_dist[n]


# Describe your graph here
Graph_nodes = {
    'S': [('OBS', 1), ('7', 1), ('OBS', 1)],
    '3': [('OBS', 1), ('4', 1), ('OBS', 1), ('9', 1), ('10', 1)],
    '4': [('3', 1), ('9', 1), ('OBS', 1), ('10', 1)],
    '43': [('12', 1), ('OBS', 1), ('OBS', 1), ('G', 1), ('44', 1)],
    '7': [('S', 1), ('14', 1), ('13', 1), ('OBS', 1), ('OBS', 1)],
    '9': [('OBS', 1), ('OBS', 1), ('14', 1), ('15', 1), ('16', 1), ('10', 1), ('4', 1), ('3', 1)],
    '10': [('OBS', 1), ('OBS', 1), ('4', 1), ('3', 1), ('9', 1), ('15', 1), ('16', 1), ('OBS', 1)],
    '12': [('OBS', 1), ('OBS', 1), ('OBS', 1), ('43', 1), ('18', 1), ('44', 1), ('45', 1), ('G', 1)],
    '13': [('7', 1), ('OBS', 1), ('14', 1), ('20', 1), ('19', 1)],
    '14': [('OBS', 1), ('7', 1), ('13', 1), ('19', 1), ('20', 1), ('OBS', 1), ('15', 1), ('9', 1)],
    '15': [('9', 1), ('OBS', 1), ('14', 1), ('20', 1), ('OBS', 1), ('22', 1), ('16', 1), ('10', 1)],
    '16': [('10', 1), ('9', 1), ('15', 1), ('OBS', 1), ('22', 1), ('OBS', 1), ('OBS', 1), ('OBS', 1)],
    '18': [('12', 1), ('OBS', 1), ('OBS', 1), ('OBS', 1), ('24', 1), ('44', 1), ('45', 1), ('46', 1)],
    '19': [('13', 1), ('14', 1), ('20', 1), ('25', 1), ('26', 1)],
    '20': [('14', 1), ('13', 1), ('19', 1), ('25', 1), ('26', 1), ('OBS', 1), ('OBS', 1), ('15', 1)],
    '22': [('16', 1), ('15', 1), ('OBS', 1), ('OBS', 1), ('28', 1), ('29', 1), ('OBS', 1), ('OBS', 1)],
    '24': [('18', 1), ('OBS', 1), ('OBS', 1), ('29', 1), ('30', 1), ('45', 1), ('46', 1), ('47', 1)],
    '25': [('19', 1), ('20', 1), ('26', 1), ('32', 1), ('31', 1)],
    '26': [('20', 1), ('19', 1), ('25', 1), ('31', 1), ('32', 1), ('OBS', 1), ('OBS', 1), ('OBS', 1)],
    '28': [('22', 1), ('OBS', 1), ('OBS', 1), ('OBS', 1), ('34', 1), ('35', 1), ('29', 1), ('OBS', 1)],
    '29': [('OBS', 1), ('22', 1), ('28', 1), ('34', 1), ('35', 1), ('36', 1), ('30', 1), ('24', 1)],
    '30': [('24', 1), ('OBS', 1), ('29', 1), ('35', 1), ('36', 1), ('46', 1), ('47', 1), ('48', 1)],
    '31': [('25', 1), ('26', 1), ('32', 1), ('37', 1), ('38', 1)],
    '32': [('26', 1), ('25', 1), ('31', 1), ('37', 1), ('38', 1), ('OBS', 1), ('OBS', 1), ('OBS', 1)],
    '34': [('28', 1), ('OBS', 1), ('OBS', 1), ('OBS', 1), ('40', 1), ('41', 1), ('35', 1), ('29', 1)],
    '35': [('29', 1), ('28', 1), ('34', 1), ('40', 1), ('41', 1), ('42', 1), ('36', 1), ('30', 1)],
    '36': [('30', 1), ('29', 1), ('35', 1), ('41', 1), ('42', 1), ('47', 1), ('48', 1), ('49', 1)],
    '37': [('31', 1), ('32', 1), ('38', 1)],
    '38': [('31', 1), ('32', 1), ('37', 1), ('OBS', 1), ('OBS', 1)],
    '40': [('34', 1), ('35', 1), ('41', 1), ('OBS', 1), ('OBS', 1)],
    '41': [('34', 1), ('40', 1), ('35', 1), ('36', 1), ('42', 1)],
    '42': [('36', 1), ('41', 1), ('35', 1), ('48', 1), ('49', 1)],
    'G': [('43', 1), ('12', 1), ('44', 1)],
    '44': [('G', 1), ('43', 1), ('12', 1), ('18', 1), ('45', 1)],
    '45': [('44', 1), ('12', 1), ('18', 1), ('24', 1), ('46', 1)],
    '46': [('45', 1), ('18', 1), ('24', 1), ('30', 1), ('47', 1)],
    '47': [('46', 1), ('24', 1), ('30', 1), ('36', 1), ('48', 1)],
    '48': [('47', 1), ('30', 1), ('36', 1), ('42', 1), ('49', 1)],
    '49': [('48', 1), ('36', 1), ('42', 1)]
}

aStarAlgo('S', 'G')
