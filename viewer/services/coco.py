import json
from collections import defaultdict

class CocoDataset:
    def __init__(self, annotation_file):
        with open(annotation_file) as f:
            coco = json.load(f)

        self.images = {i['id']: i for i in coco['images']}
        self.categories = {c['id']: c for c in coco['categories']}

        self.annotations_by_image = defaultdict(list)
        for a in coco['annotations']:
            self.annotations_by_image[a['image_id']].append(a)
