class MultiHashSet:
    INITIAL_BUCKETS_SIZE: int = 16
    INCREASE_FACTOR: int = 2
    PAYLOAD_FACTOR = 0.75

    def __init__(self):
        """Hasch list creator

        """
        self.buckets: list = [[] for _i in range(self.INITIAL_BUCKETS_SIZE)]
        self.length = 0

    def add(self, new_entry):
        if self.length / len(self.buckets) > self.PAYLOAD_FACTOR:
            self._increase_bucket_count()
        new_entry_hash = hash(new_entry)
        bucket_index = new_entry_hash % len(self.buckets)
        self.buckets[bucket_index].append(new_entry)
        self.length += 1

    def remove(self, to_remove):
        to_remove_hash = hash(to_remove)
        bucket_index = to_remove_hash % len(self.buckets)
        if to_remove in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(to_remove)

    def remove_all(self, item):
        item_bucket = hash(item) % len(self.buckets)
        bucket = self.buckets[item_bucket]
        self.buckets[item_bucket] = [x for x in bucket if x != item]
        self.length = len(bucket) - len(self.buckets[item_bucket])

    def __len__(self):
        return self.length

    def add_all(self, elements):
        for element in elements:
            self.add(element)

    # TA FUNCJA POWINNA SIE ZMIENIĆ
    def _increase_bucket_count(self)
        new_buckets = [[] for _i in range(self.INCREASE_FACTOR * len(self.buckets))]
        for old_bucket in self.buckets:
            for element in old_bucket:
                new_bucket_index = hash(element) % len(new_buckets)
                new_buckets[new_bucket_index].append(element)
        self.buckets = new_buckets

    def clear(self):
        for bucket in self.buckets:
            bucket.clear()
        self.length = 0

    def contains(self, item):
        item_bucket_index = hash(item) % len(self.buckets)
        return item in self.buckets[item_bucket_index]

    def __contains__(self, item):
        return self.contains(item)

    def __str__(self):
        result = '{'
        for bucket in self.buckets:
            for element in bucket:
                result += str(element)
                result += ", "
        result = result[:-2]
        result += '}'
        return result

    def my_clear(self):
        self.buckets = []

    def __hash__(self):
        pass

    def __eq__(self, other):
        this = self._group_elements(self)
        that = self._group_elements(other)
        return this == that

    @staticmethod
    def _group_elements(mhs):
        elements = []
        for bucket in mhs.buckets:
            for element in bucket:
                elements.append(element)
        elements_grouped_by = dict()
        for element in elements:
            if element not in elements_grouped_by:
                elements_grouped_by[element] = 0
            elements_grouped_by[element] += 1
        return elements_grouped_by