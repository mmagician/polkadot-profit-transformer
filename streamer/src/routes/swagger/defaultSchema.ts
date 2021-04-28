const errorResponse = {
  type: 'object',
  properties: {
    code: { type: 'number' },
    message: { type: 'string', nullable: true }
  }
}

export {
  errorResponse
}
