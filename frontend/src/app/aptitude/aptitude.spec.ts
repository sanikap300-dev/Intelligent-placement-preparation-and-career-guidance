import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Aptitude } from './aptitude';

describe('Aptitude', () => {
  let component: Aptitude;
  let fixture: ComponentFixture<Aptitude>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Aptitude],
    }).compileComponents();

    fixture = TestBed.createComponent(Aptitude);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
