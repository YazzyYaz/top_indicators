from top_indicators import *


def test_sopr():
  result = sopr()

  assert result.remaining is not None


def test_price_from_prev_top():
  result = price_from_previous_top()

  assert result.remaining is not None


def test_average_fee():
  result = average_fee()

  assert result.remaining is not None


def test_mvrv():
  result = mvrv()

  assert result.remaining is not None


def test_gbtc():
  result = gbtc()

  assert result.remaining is not None


def test_metric_completion():
  result = Metric("","", current=1, target=2)

  assert result.completion == 0.5


def test_progress_bar():
  result = Metric("","", current=1, target=2)

  assert result.progress_bar == "|##################################################--------------------------------------------------| 50.0%"