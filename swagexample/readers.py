"""A dataset reader for SWAG."""

import csv
import logging
from overrides import overrides
from typing import (
    Dict,
    Optional)

from allennlp.common import Params
from allennlp.common.file_utils import cached_path
from allennlp.data.dataset_readers.dataset_reader import DatasetReader
from allennlp.data.fields import LabelField, TextField
from allennlp.data.instance import Instance
from allennlp.data.tokenizers import Tokenizer, WordTokenizer
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer


logger = logging.getLogger(__name__)


@DatasetReader.register("swag")
class SWAGDatasetReader(DatasetReader):
    """Read in the SWAG dataset for AllenNLP models.

    The SWAG dataset should be formatted as a CSV with startphrase,
    ending0 - ending3, and optional label columns all labeled with a
    header row.

    Parameters
    ----------
    lazy : ``bool``, (optional, default=``False``)
        Whether or not to read the dataset in a lazy fashion. If
        ``True``, batches will take longer but training will begin
        faster. For larger-than-memory datasets, use the lazy option.
    tokenizer : ``Tokenizer``, optional
        Tokenizers for the text.
    token_indexers : ``Dict[str, TokenIndexer]``, optional
        Token indexers. Defaults to
        ``{'tokens': SingleIdTokenIndexer()}``.
    """

    def __init__(
            self,
            lazy: bool=False,
            tokenizer: Tokenizer=None,
            token_indexers: Dict[str, TokenIndexer]=None
    ) -> None:
        super().__init__(lazy)
        self.tokenizer = tokenizer or WordTokenizer()
        self.token_indexers = token_indexers or {
            'tokens': SingleIdTokenIndexer()
        }

    @overrides
    def _read(self, file_path):
        with open(cached_path(file_path), 'r') as data_file:
            logger.info(f'Reading {file_path}.')
            csv_reader = csv.DictReader(data_file)
            for row in csv_reader:
                yield self.text_to_instance(
                    startphrase=row['startphrase'],
                    ending0=row['ending0'],
                    ending1=row['ending1'],
                    ending2=row['ending2'],
                    ending3=row['ending3'],
                    label=row.get('label'))

    @overrides
    def text_to_instance(
            self,
            startphrase: str,
            ending0: str,
            ending1: str,
            ending2: str,
            ending3: str,
            label: Optional[int]=None
    ) -> Instance:
        fields = {
            'startphrase': TextField(
                self.tokenizer.tokenize(startphrase),
                self.token_indexers),
            'ending0': TextField(
                self.tokenizer.tokenize(ending0),
                self.token_indexers),
            'ending1': TextField(
                self.tokenizer.tokenize(ending1),
                self.token_indexers),
            'ending2': TextField(
                self.tokenizer.tokenize(ending2),
                self.token_indexers),
            'ending3': TextField(
                self.tokenizer.tokenize(ending3),
                self.token_indexers)
        }
        if label is not None:
            fields['label'] = LabelField(label)

        return Instance(fields)

    @classmethod
    def from_params(cls, params: Params) -> 'SWAGDatasetReader':
        lazy = params.pop('lazy', False)
        tokenizer = Tokenizer.from_params(params.pop('tokenizer', {}))
        token_indexers = TokenIndexer.dict_from_params(
            params.pop('token_indexers', {}))
        params.assert_empty(cls.__name__)

        return cls(
            lazy=lazy,
            tokenizer=tokenizer,
            token_indexers=token_indexers)
