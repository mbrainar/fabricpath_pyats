from virl2_client import ClientLibrary
from config import host, username, password, lab_id
from pprint import pprint

def connect(host, username, password):
    client = ClientLibrary(host, username, password, ssl_verify=False)
    client.wait_for_lld_connected()
    return client

def join_lab(client, lab_id):
    lab = client.join_existing_lab(lab_id)
    return lab

def get_nodes(lab):
    return lab.nodes()

def main():
    client = connect(host, username, password)
    lab = join_lab(client, lab_id)
    # print(lab.title)
    nodes = get_nodes(lab)
    print(nodes)
    for node in nodes:
        print(node.nid())


if __name__ == "__main__":
    main()
