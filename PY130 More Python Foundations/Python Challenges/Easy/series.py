# - Initialize series to empty list.
# - Initialize start_idx to 0
# - Initialize end_idx to slice length - 1
# - while end_idx is less than equal to length of the input string:
#       - current string = original string[start_idx:end_idx]
#       - Append each character as integer in separate list and append
#         that list to series
#       - Increase start_idx and end_idx by 1.
# - Return series

class Series:
    def __init__(self, string_num):
        self._string_num = string_num

    def slices(self, slice_length):
        if slice_length > len(self._string_num):
            raise ValueError("Slice length is greater than string length")

        all_series = []
        start_idx = 0
        end_idx = slice_length

        while end_idx <= len(self._string_num):
            current_series_string = self._string_num[start_idx:end_idx]
            current_series_lst = [int(num_str) 
                                  for num_str in current_series_string]
            all_series.append(current_series_lst)
            start_idx += 1
            end_idx += 1

        return all_series
