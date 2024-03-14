# cCONF: Global constants endpoint structure

BODY_METHODS = ["POST", "PATCH"]

NO_PARAM_METHOD_TEMPLATE = {
	"query_params": {},
	"body_params": {},
}

ENDPOINTS = {
	"/login": {
		"methods": {
			"POST": {
				"content_type": "application/json", 
				"query_params": {
					"remember": {
						"type": "boolean",
						"required": False,
						"default": False,
						"description": "If false, the session will be deleted after the browser is closed"
					}
				},
				"body_params": {
					"username": {
						"type": "string",
						"required": True,
						"description": "Username of the user"
					}, 
					"password": {
						"type": "string",
						"required": True,
						"description": "Password of the user"
					}
				},
			}
		}
	}, "/logout": {
		"methods": {
			"POST": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/authenticate": {
		"methods": {
			"POST": {
				"content_type": "application/json",
				"query_params": {
				},
				"body_params": {
					"username": {
						"type": "string",
						"required": True,
						"description": "Username of the user"
					},
					"password": {
						"type": "string",
						"required": True,
						"description": "Password of the user"
					}
				},
			}
		}
	}, "/users/me": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"PATCH": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"nickname": {
						"type": "string",
						"required": False,
						"description": "Nickname of the user"
					}, "password": {
						"type": "string",
						"required": False,
						"description": "Password of the user"
					}, "tournament_id": {
						"type": "integer",
						"required": False,
						"description": "ID of the tournament joined"
					}
				},
			}, "DELETE": NO_PARAM_METHOD_TEMPLATE
		}
	}, "/users/me/avatar": {
		"methods": {
			"POST": {
				"query_params": {},
				"body_params": {}
			}
		}
	}, "/users/me/blocked": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"user_id": {
						"type": "id",
						"required": True,
						"description": "ID of the user to block"
					}
				},
			}
		}
	}, "/users/me/blocked/USER_ID": {
		"methods": {
			"DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/me/channels": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/me/friends": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/me/friends/USER_ID": {
		"methods": {
			"DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/me/friends/requests": {
		"methods": {
			"GET": {
				"query_params": {
					"type": {
						"type": "string",
						"required": False,
						"default": "all",
						"description": "Type of the friend requests returned (all, sent, received)"
					}
				},
				"body_params": {},
			}, "POST": {
				"content_type": "application/json", 
				"query_params": {},
				"body_params": {
					"nickname": {
						"type": "string",
						"required": True,
						"description": "Nickname of the user to send the friend request to"
					}
				},
			}
		}
	}, "/users/me/friends/requests/REQUEST_ID": {
		"methods": {
			"POST": NO_PARAM_METHOD_TEMPLATE,
			"DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/me/notifications": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"type": {
						"type": "string",
						"required": True,
						"description": "Type of the notification"
					}, "content": {
						"type": "string",
						"required": True,
						"description": "Content of the notification"
					}
				},
			}
		}
	}, "/users/me/notifications/NOTIFICATION_ID": {
		"methods": {
			"DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"username": {
						"type": "string",
						"required": True,
						"description": "Username of the user"
					}, "password": {
						"type": "string",
						"required": True,
						"description": "Password of the user"
					}
				},
			}
		}
	}, "/users/USER_ID": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"PATCH": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"nickname": {
						"type": "string",
						"required": False,
						"description": "Nickname of the user"
					}, "password": {
						"type": "string",
						"required": False,
						"description": "Password of the user"
					}
				},
			}, "DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/USER_ID/avatar": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/users/USER_ID/games": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
		}
		}, "/users/USER_ID/games_upcoming": {
		"methods": {
			"GET": {
				"description": "Games with status created, i.e. not yet started",
				"query_params": {},
				"body_params": {},
			},
		}
	}, "/tournaments": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"title": {
						"type": "string",
						"required": True,
						"description": "Title of the tournament"
					}, "description": {
						"type": "string",
						"required": False,
						"description": "Description of the tournament"
					}
				},
			}
		}
	}, "/tournaments/TOURNAMENT_ID": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"DELETE": NO_PARAM_METHOD_TEMPLATE,
			"PATCH": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"title": {
						"type": "string",
						"required": False,
						"description": "Title of the tournament"
					}, "description": {
						"type": "string",
						"required": False,
						"description": "Description of the tournament"
					}, "status": {
						"type": "string",
						"required": False,
						"description": "'next' -> advance to next tournament status, 'cancelled' -> cancel tournament"
					}
				},
			}
		}
    }, "/tournaments/TOURNAMENT_ID/play": {
		"methods": {
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"play": {
						"type": "string",
						"required": True,
						"description": "join on unjoin the tournament"
					},
				}
			},
		}
	}, "/tournaments/TOURNAMENT_ID/games": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/tournaments/TOURNAMENT_ID/games/GAME_ID": {
        "methods": {
            "GET": NO_PARAM_METHOD_TEMPLATE,
            "DELETE": NO_PARAM_METHOD_TEMPLATE,
            "PATCH": {
                "content_type": "application/json",
				"query_params": {},
				"body_params": {
					"player1_score": {
						"type": "integer",
						"required": False,
						"description": "Score of the first player"
					}, "player2_score": {
						"type": "integer",
						"required": False,
						"description": "Score of the second player"
					}
					#}, "status": {
					#	"type": "string",
					#	"required": False,
					#	"description": "Status of the game"
					#}
				},
			}
		}
	}, "/games": {
		"methods": {
			#"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"tournament_id": {
						"type": "id",
						"required": False,
						"default": "null",
						"description": "ID of the tournament"
					}, "player1_id": {
						"type": "id",
						"required": True,
						"description": "ID of the first player"
					}, "player2_id": {
						"type": "id",
						"required": True,
						"description": "ID of the second player"
					}, "player1_score": {
						"type": "integer",
						"required": False,
						"default": 0,
						"description": "Score of the first player"
					}, "player2_score": {
						"type": "integer",
						"required": False,
						"default": 0,
						"description": "Score of the second player"
					}
				},
			}
		}
	}, "/games/GAME_ID": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"PATCH": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"player1_score": {
						"type": "integer",
						"required": False,
						"description": "Score of the first player"
					}, "player2_score": {
						"type": "integer",
						"required": False,
						"description": "Score of the second player"
					}, "status": {
						"type": "string",
						"required": False,
						"description": "Status of the game"
					}
				},
			}, "DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/channels": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"name": {
						"type": "string",
						"required": True,
						"description": "Name of the channel"
					}
				},
			}
		}
	}, "/channels/CHANNEL_ID": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"PATCH": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"name": {
						"type": "string",
						"required": False,
						"description": "Name of the channel"
					}
				},
			}, "DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/channels/CHANNEL_ID/members": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"user_id": {
						"type": "id",
						"required": True,
						"description": "ID of the user to add to the channel"
					}
				},
			}
		}
	}, "/channels/CHANNEL_ID/members/USER_ID": {
		"methods": {
			"DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/channels/CHANNEL_ID/messages": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
			"POST": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"content": {
						"type": "string",
						"required": True,
						"description": "Content of the message"
					}
				},
			}
		}
	}, "/messages": {
		"methods": {
			"GET": NO_PARAM_METHOD_TEMPLATE,
		}
	}, "/messages/MESSAGE_ID": {
		"methods": {
			"PATCH": {
				"content_type": "application/json",
				"query_params": {},
				"body_params": {
					"content": {
						"type": "string",
						"required": True,
						"description": "Content of the message"
					}
				},
			}, "DELETE": NO_PARAM_METHOD_TEMPLATE,
		}
	} 
}
