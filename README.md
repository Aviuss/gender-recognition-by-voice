# Init

Create folder
`mkdir ./train`
and put there audio files in format `XXXX_?.waw`, where `?` is `M`(male) or `K`(female)

# Results

> Males: 85-180Hz
> Females: 165-255Hz

### Get gender from highest frequency in human base range 

function: `get_gender_from_highest_freq_in_range(sample_rate, data, n, freqs, single_channel, apply_window=True/False)`

It filters frequencies in range 85-255 and then select's the highest. Based on threshold it selects when its male or female.

```
threshold = XXX
selected_gender = None
if dominant_freq > threshold:
    selected_gender = "K"
else:
    selected_gender = "M"
```

Test set length: 91 audio recordings

Without window function:
threshold => accuracy
150 => 73.63 %
160 => 73.63 %
170 => 75.82 %
175 => 76.92 %
176 => 76.92 %
177 => 76.92 %
180 => 74.73 %
190 => 74.73 %
195 => 75.82 %
197 => 75.82 %
198 => 76.92 %
199 => 76.92 %
200 => 76.92 %
201 => 75.82 %
202 => 75.82 %
203 => 75.82 %
205 => 76.92 %
206 => 78.02 % best
207 => 75.82 %
210 => 73.63 %
220 => 69.23 %

With window function:
threshold => accuracy
150 => 75.82 %
160 => 76.92 %
170 => 78.02 %
174 => 79.12 %
175 => 79.12 % best
176 => 79.12 %
180 => 79.12 %
190 => 76.92 %
200 => 76.92 %
205 => 76.92 %
210 => 75.82 %