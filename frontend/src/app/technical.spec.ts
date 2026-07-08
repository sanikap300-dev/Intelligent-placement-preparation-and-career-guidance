import { TestBed } from '@angular/core/testing';

import { Technical } from './technical';

describe('Technical', () => {
  let service: Technical;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Technical);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
