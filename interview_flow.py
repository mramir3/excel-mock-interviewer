QUESTIONS = [
    {"id": "q_sum", "text": "Compute total sales from 'Sales' column.", "file_required": True, "ground_truth": {"action": "sum", "column": "Sales"}},
    {"id": "q_avg", "text": "Filter Region='West' and average 'Revenue'.", "file_required": True, "ground_truth": {"action": "filter_avg", "filter": {"Region": "West"}, "column": "Revenue"}},
    {"id": "q_vlookup", "text": "Join Orders and Customers by CustomerID. Which formula would you use?", "file_required": True, "ground_truth": {"action": "join", "left_key": "CustomerID", "right_key": "CustomerID"}}
]
