def update_model(model, in_parameters):
  for key, value in in_parameters.items():
    setattr(model, key, value)
  model.save()
  return model