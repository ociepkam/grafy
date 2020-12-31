import random


def prepare_randomized_experiment(data, config):
    print(data)
    new_data = []
    for edge in [3, 4, 5]:
        if config["no_of_edges"][str(edge)]:
            temp_edge = [elem for elem in data if len(elem["EA"]) == edge]
            for crossed, bool_v in [["graphs_with_crossed", "yes"], ["graphs_without_crossed_edges", "no"]]:
                if config["crossed_edges"][crossed]:
                    temp_crossed = [elem for elem in temp_edge if elem["Crossed_edges"] == bool_v]
                    for types_of_vertices, name in [["direct", "DI"], ["indirect", "inDI"]]:
                        if config["types_of_target_vertices"][types_of_vertices]:
                            trials = [elem for elem in temp_crossed if elem["Type"] == name]
                            assert len(trials) > 0, "No trials with edge={}, crossed={}, types_of_target_vertices={}".format(edge, crossed, name)
                            random.shuffle(trials)
                            i = 0
                            while i < config["trials_per_cell"]:
                                if len(trials) < config["trials_per_cell"] - i:
                                    new_data.append(trials)
                                    i += len(trials)
                                else:
                                    new_data.append(trials[:config["trials_per_cell"] - i])
                                    i += (config["trials_per_cell"] - i)

    new_data = [item for sub_list in new_data for item in sub_list]
    return new_data