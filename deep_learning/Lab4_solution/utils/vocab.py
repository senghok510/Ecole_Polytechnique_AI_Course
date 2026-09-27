from typing import Dict, List, Optional


class Vocab():
    
    def __init__(self, vocab) -> None:
        i=0
        v={}
        for key in vocab.keys():
            v[key]=i
            i+=1
        v['<unk>']=i
        v['<pad>']=i+1
            
        self.vocab = v

    def forward(self, tokens: List[str]) -> List[int]:
        r"""
        Args:
            tokens: a list of tokens used to lookup their corresponding `indices`.

        Returns:
            The indices associated with a list of `tokens`.
        """
        ret=[]
        for t in tokens:
            try:
                idx = self.vocab[t]
            except:
                idx = self.vocab['<unk>']
            ret.append(idx)
        
        return ret

    def __len__(self) -> int:
        r"""
        Returns:
            The length of the vocab.
        """
        return len(self.vocab)
    
    def getPadding(self) -> int:
        return self.vocab['<pad>']
    
    def __contains__(self, token: str) -> bool:
        r"""
        Args:
            token: The token for which to check the membership.

        Returns:
            Whether the token is member of vocab or not.
        """
        return self.vocab.__contains__(token)

    def __getitem__(self, token: str) -> int:
        r"""
        Args:
            token: The token used to lookup the corresponding index.

        Returns:
            The index corresponding to the associated token.
        """
        return self.vocab[token]


    def lookup_indices(self, tokens: List[str]) -> List[int]:
        r"""
        Args:
            tokens: the tokens used to lookup their corresponding `indices`.

        Returns:
            The 'indices` associated with `tokens`.
        """
        return self.forward(tokens)
